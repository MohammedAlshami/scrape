"""CLI entry point for Python ops called from Next.js API routes."""

import json, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def get_scraper(source: str = ""):
    """Get scraper instance by name or default to malaymail."""
    from tools.news.sources import SCRAPERS
    if source and source in SCRAPERS:
        return SCRAPERS[source]()
    return SCRAPERS["malaymail"]()


def cmd_article():
    source = sys.argv[2] if len(sys.argv) > 3 else ""
    url = sys.argv[3] if len(sys.argv) > 3 else sys.argv[2]
    news = get_scraper(source)
    art = news.get_article(url)
    if not art:
        print(json.dumps({"error": "not found"}))
        sys.exit(1)
    print(json.dumps({
        "title": art.title,
        "url": art.url,
        "source": art.source,
        "published_at": str(art.published_at) if art.published_at else None,
        "author": art.author,
        "categories": art.categories,
        "image_url": art.image_url,
        "summary": art.summary,
        "content": [
            {"type": b.type.value if hasattr(b.type, "value") else b.type,
             "text": b.text, "children": b.children, "src": b.src, "alt": b.alt}
            for b in art.content
        ],
    }))


def cmd_scrape():
    from database import Database
    source = sys.argv[2] if len(sys.argv) > 3 else ""
    query = sys.argv[3] if len(sys.argv) > 3 else (sys.argv[2] if len(sys.argv) > 2 else "malaysia politics")
    news = get_scraper(source)
    db = Database(password="password")
    results = news.search(query, max_results=12)
    count = 0
    for r in results:
        exists = db.query("MATCH (n:Article) WHERE n.url = $url RETURN count(n) AS c", url=r.url)
        if exists[0]["c"] > 0:
            continue
        art = news.get_article(r.url)
        if not art:
            continue
        db.query(
            "CREATE (n:Article {title: $title, url: $url, source: $source, "
            "published_at: $published_at, author: $author, categories: $categories, "
            "image_url: $image_url, summary: $summary})",
            title=art.title, url=art.url, source=art.source,
            published_at=str(art.published_at) if art.published_at else None,
            author=art.author or "", categories=",".join(art.categories),
            image_url=art.image_url or "", summary=art.summary or "",
        )
        count += 1
    print(json.dumps({"scraped": count, "total": len(results)}))


def cmd_chat():
    from ai import chat as ai_chat
    messages = json.loads(sys.stdin.read())
    result = ai_chat(messages)
    print(json.dumps({"content": result}))


def cmd_test_scraper():
    """Test a specific scraper: python tools/run.py test_scraper <source> [query]"""
    source = sys.argv[2] if len(sys.argv) > 2 else "malaymail"
    query = sys.argv[3] if len(sys.argv) > 3 else "politics"
    news = get_scraper(source)
    print(f"Testing {source} scraper...", file=sys.stderr)
    results = news.search(query, max_results=3)
    if not results:
        print(json.dumps({"error": "no search results", "source": source}))
        sys.exit(1)
    out = []
    for r in results:
        art = news.get_article(r.url)
        out.append({
            "title": art.title if art else r.title,
            "url": r.url,
            "has_content": art is not None and len(art.content) > 0,
            "paragraphs": len(art.content) if art and art.content else 0,
            "image_url": r.image_url,
        })
    print(json.dumps({"source": source, "results": out}, default=str))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "no command"}))
        sys.exit(1)

    command = sys.argv[1]

    if command == "article":
        cmd_article()
    elif command == "scrape":
        cmd_scrape()
    elif command == "chat":
        cmd_chat()
    elif command == "test_scraper":
        cmd_test_scraper()
    else:
        print(json.dumps({"error": f"unknown command: {command}"}))
        sys.exit(1)
