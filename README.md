# Scrape — Malaysian Political Discovery

Parallel, resumable scrapers for Malaysian political content. Searches 5 news
sources (MalayMail, Astro Awani, Sinar Daily, Dayak Daily, Twentytwo13) +
Wikipedia using year-specific queries. Designed for election prediction research.

## Usage

```bash
# install deps
pip install requests beautifulsoup4 lxml wikipedia-api

# run any scraper (Ctrl+C safe — re-run to resume)
python scrape/policies_discovery.py --all
python scrape/anwar_discovery.py --all
python scrape/umno_discovery.py
python scrape/parliament_monitor.py
```

All scripts save results to their own folder (e.g. `/policies/`, `/anwar_ibrahim/`)
with `_metadata.json` and `_progress.json` for deduplication and resume.

## Scrapers

See `scrape/scraper_base.py` for the shared engine. Each `*_discovery.py` is just
a config wrapper (keywords, topics, Wikipedia pages).
