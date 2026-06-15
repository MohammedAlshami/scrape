"""
Shared resumable discovery engine — used by all scrape scripts.
Each script just imports this and calls run() with its config.
"""

import json, os, sys, time, re, threading, signal
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

_meta_lock = threading.Lock()
_progress_lock = threading.Lock()
_abort = threading.Event()


def on_sigint(signum, frame):
    print("\n\nCaught Ctrl+C. Saving progress and exiting cleanly...")
    _abort.set()

signal.signal(signal.SIGINT, on_sigint)


def safe_filename(title: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "", title).strip()[:150]
    return name or "untitled"


def parse_date(date_str: str) -> datetime | None:
    if not date_str:
        return None
    for fmt in (
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%d/%m/%Y",
    ):
        try:
            d = datetime.strptime(date_str.replace("Z", ""), fmt)
            return d.replace(tzinfo=timezone.utc) if d.tzinfo is None else d
        except ValueError:
            continue
    try:
        d = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return d
    except:
        pass
    return None


def load_json(path: str) -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_json(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def _is_saved(meta_file: str, url: str) -> bool:
    with _meta_lock:
        return url in load_json(meta_file)


def _mark_saved(meta_file: str, output_dir: str, url: str, title: str, source: str, date: str, filepath: str):
    with _meta_lock:
        meta = load_json(meta_file)
        meta[url] = {
            "title": title,
            "source": source,
            "date": date,
            "filepath": os.path.relpath(filepath, output_dir),
            "saved_at": datetime.now(timezone.utc).isoformat(),
        }
        save_json(meta_file, meta)


def _save_progress(progress_file: str, p: dict):
    with _progress_lock:
        save_json(progress_file, p)


def save_article_md(output_dir: str, title: str, source: str, date: str, url: str, body: str, categories: list[str] | None = None):
    filename = f"{safe_filename(title)}.md"
    filepath = os.path.join(output_dir, filename)
    cat_line = f"  - {', '.join(categories)}\n" if categories else ""
    md = f"""# {title}

- **Source**: {source}
- **Date**: {date}
- **URL**: {url}
{cat_line}
---
{body}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    return filepath


# ── Search phase ───────────────────────────────────────────────────

def _search_one(scraper_name: str, scraper_cls, query: str, keywords: list[str]) -> list:
    try:
        scraper = scraper_cls()
        results = scraper.search(query, max_results=10)
        lower_kw = [k.lower() for k in keywords]
        out = []
        for r in results:
            rlow = r.title.lower()
            if any(k in rlow for k in lower_kw):
                out.append((r.url, r.title, scraper_name))
        return out
    except Exception:
        return []


def gather_all_urls(meta_file: str, progress_file: str, output_dir: str,
                    keywords: list[str], topics: list[str],
                    from_year: int, to_year: int,
                    workers: int = 30) -> list[tuple[str, str, str]]:
    from tools.news.sources import SCRAPERS

    progress = load_json(progress_file)
    done_queries = set(progress.get("search_done", []))

    all_tasks = []
    for q in topics:
        for year in range(from_year, to_year + 1):
            for sname in SCRAPERS:
                key = f"{sname}|{q}|{year}"
                all_tasks.append((key, sname, SCRAPERS[sname], f"{q} {year}"))

    if progress.get("search_complete"):
        stored = progress.get("url_list", [])
        print(f"  Search already done ({len(stored)} candidates)")
        return stored

    remaining = [t for t in all_tasks if t[0] not in done_queries]
    total_all = len(all_tasks)
    print(f"\n  Firing {len(remaining)}/{total_all} remaining search requests...")

    seen = set()
    all_urls: list[tuple[str, str, str]] = []
    done = 0

    with ThreadPoolExecutor(max_workers=workers) as pool:
        fut_map = {}
        for key, sname, scls, q in all_tasks:
            if _abort.is_set():
                break
            if key not in done_queries:
                fut = pool.submit(_search_one, sname, scls, q, keywords)
                fut_map[fut] = (key, sname, q)

        for fut in as_completed(fut_map):
            if _abort.is_set():
                break
            done += 1
            key, sname, q = fut_map[fut]
            try:
                for url, title, src in fut.result():
                    if url not in seen:
                        seen.add(url)
                        all_urls.append((url, title, src))
            except Exception:
                pass
            done_queries.add(key)

            if done % 20 == 0:
                p = load_json(progress_file)
                p["phase"] = "search"
                p["search_done"] = list(done_queries)
                p["search_progress"] = f"{done}/{total_all}"
                p["search_urls"] = len(all_urls)
                p["url_list"] = all_urls
                _save_progress(progress_file, p)
                print(f"    Searches: {done}/{total_all}  |  Unique URLs: {len(all_urls)}")

    if _abort.is_set():
        p = load_json(progress_file)
        p["phase"] = "search"
        p["search_done"] = list(done_queries)
        p["search_progress"] = f"{done}/{total_all}"
        p["search_urls"] = len(all_urls)
        p["url_list"] = all_urls
        _save_progress(progress_file, p)
        print("  Saved search progress. Re-run to continue.")
        sys.exit(0)

    p = load_json(progress_file)
    p["phase"] = "search_done"
    p["search_complete"] = True
    p["search_done"] = list(done_queries)
    p["search_urls"] = len(all_urls)
    p["url_list"] = all_urls
    _save_progress(progress_file, p)

    print(f"    Done. {len(all_urls)} unique candidates from {done} searches")
    return all_urls


# ── Read phase ─────────────────────────────────────────────────────

def _read_and_save_one(meta_file: str, output_dir: str, keywords: list[str],
                       url: str, title: str, source: str,
                       start: datetime, end: datetime) -> int:
    if _is_saved(meta_file, url):
        return 0
    try:
        from tools.news.sources import SCRAPERS
        scraper = SCRAPERS[source]()
        art = scraper.get_article(url)
        if not art or not art.title:
            return 0

        pub_date = parse_date(str(art.published_at)) if art.published_at else None
        if pub_date is None or pub_date < start or pub_date > end:
            return 0

        blocks = []
        for b in art.content:
            t = b.text.strip() if b.text else ""
            if t:
                blocks.append(t)
            if b.children:
                for c in b.children:
                    if isinstance(c, str):
                        blocks.append(c.strip())
        body = "\n\n".join(blocks) if blocks else (art.summary or "")

        lower_kw = [k.lower() for k in keywords]
        if not any(k in body.lower() for k in lower_kw):
            return 0

        date_str = str(art.published_at) if art.published_at else ""
        fp = save_article_md(output_dir, art.title, source, date_str, url, body, art.categories)
        _mark_saved(meta_file, output_dir, url, art.title, source, date_str, fp)
        return 1
    except Exception:
        return 0


def read_and_save_all(meta_file: str, progress_file: str, output_dir: str,
                      keywords: list[str],
                      urls: list[tuple[str, str, str]],
                      start: datetime, end: datetime,
                      workers: int = 25) -> int:
    progress = load_json(progress_file)
    if progress.get("read_complete"):
        saved = progress.get("read_saved", 0)
        print(f"  Read phase already done ({saved} saved)")
        return saved

    total = len(urls)
    saved = 0
    done = 0
    print(f"  Reading {total} articles with {workers} workers...")

    with ThreadPoolExecutor(max_workers=workers) as pool:
        args_list = [(meta_file, output_dir, keywords, u, t, s, start, end) for u, t, s in urls]
        fut_map = {pool.submit(_read_and_save_one, *a): a for a in args_list}
        for fut in as_completed(fut_map):
            if _abort.is_set():
                break
            done += 1
            try:
                saved += fut.result()
            except Exception:
                pass
            if done % 20 == 0 or done == total:
                p = load_json(progress_file)
                p["phase"] = "read"
                p["read_done"] = done
                p["read_total"] = total
                p["read_saved"] = saved
                _save_progress(progress_file, p)
                print(f"    Articles: {done}/{total}  |  Saved: {saved}")

    if _abort.is_set():
        print("  Saved read progress. Re-run to continue.")
        sys.exit(0)

    p = load_json(progress_file)
    p["phase"] = "read_done"
    p["read_complete"] = True
    p["read_saved"] = saved
    _save_progress(progress_file, p)
    print(f"    Done. {saved} articles saved")
    return saved


# ── Wikipedia phase ────────────────────────────────────────────────

def scrape_wikipedia(meta_file: str, progress_file: str, output_dir: str,
                     keywords: list[str], wiki_pages: list[str]) -> int:
    progress = load_json(progress_file)
    if progress.get("phase") == "wikipedia_done":
        print("  Wikipedia already done.")
        return 0

    from tools.wikipedia_tool import WikipediaTool
    wiki = WikipediaTool()
    saved = 0
    lower_kw = [k.lower() for k in keywords]

    def save_one(page_title: str) -> int:
        if _abort.is_set():
            return 0
        url = f"wikipedia:{page_title}"
        if _is_saved(meta_file, url):
            return 0
        try:
            content = wiki.content(page_title)
            if not content:
                results = wiki.search(page_title, results=3)
                if results:
                    content = wiki.content(results[0])
                    page_title = results[0]
                    url = f"wikipedia:{page_title}"
            if content and any(k in content.lower() for k in lower_kw):
                content = content[:15000]
                wp_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
                fp = save_article_md(output_dir, page_title, "wikipedia", "", wp_url, content)
                _mark_saved(meta_file, output_dir, url, page_title, "wikipedia", "", fp)
                return 1
        except Exception:
            pass
        return 0

    print(f"  Wikipedia: {len(wiki_pages)} pages...")
    with ThreadPoolExecutor(max_workers=10) as pool:
        for result in pool.map(save_one, wiki_pages):
            saved += result

    p = load_json(progress_file)
    p["phase"] = "wikipedia_done"
    p["wikipedia_saved"] = saved
    _save_progress(progress_file, p)
    print(f"    Done. {saved} pages saved")
    return saved


# ── Entry point ────────────────────────────────────────────────────

def run(name: str, output_rel: str, keywords: list[str], topics: list[str],
        wiki_pages: list[str], from_date: datetime, to_date: datetime):
    output_dir = os.path.join(ROOT, output_rel)
    os.makedirs(output_dir, exist_ok=True)
    meta_file = os.path.join(output_dir, "_metadata.json")
    progress_file = os.path.join(output_dir, "_progress.json")

    already = len(load_json(meta_file))
    total_months = (to_date.year - from_date.year) * 12 + to_date.month - from_date.month + 1
    years_range = to_date.year - from_date.year + 1

    print(f"\n{'='*60}")
    print(f" {name}")
    print(f" From: {from_date.strftime('%d %b %Y')}  To: {to_date.strftime('%d %b %Y')}")
    print(f" Years: {years_range}  |  Topics: {len(topics)}  |  Wiki: {len(wiki_pages)}")
    print(f" Already saved: {already}  |  Output: {output_dir}")
    print(f" Press Ctrl+C to stop — re-run to resume")
    print(f"{'='*60}")

    start_t = time.time()

    p = load_json(progress_file)
    phase = p.get("phase", "")

    # Gather URLs
    urls = []
    if phase in ("search", "") or not p.get("search_complete"):
        urls = gather_all_urls(meta_file, progress_file, output_dir,
                               keywords, topics,
                               from_date.year, to_date.year)
    else:
        urls = p.get("url_list", [])
    t1 = int(time.time() - start_t)
    if urls:
        print(f"\n  Search: {t1}s  |  {len(urls)} candidates")

    # Read articles
    p = load_json(progress_file)
    phase = p.get("phase", "")
    if phase in ("search_done", "read", "") or not p.get("read_complete"):
        news_saved = read_and_save_all(meta_file, progress_file, output_dir,
                                       keywords, urls, from_date, to_date)
    else:
        news_saved = p.get("read_saved", 0)
    t2 = int(time.time() - start_t)

    # Wikipedia
    p = load_json(progress_file)
    if p.get("phase") not in ("wikipedia_done",):
        wiki_saved = scrape_wikipedia(meta_file, progress_file, output_dir,
                                      keywords, wiki_pages)
    else:
        wiki_saved = p.get("wikipedia_saved", 0)
    t3 = int(time.time() - start_t)

    grand = len(load_json(meta_file))
    print(f"\n{'='*60}")
    print(f" COMPLETE in {t3}s")
    print(f" News: {news_saved}  |  Wikipedia: {wiki_saved}  |  Total: {grand}")
    print(f" Output: {output_dir}")
    print(f"{'='*60}")
