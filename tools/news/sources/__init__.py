from .malaymail import MalayMailScraper
from .astroawani import AstroAwaniScraper
from .sinardaily import SinarDailyScraper
from .dayakdaily import DayakDailyScraper
from .twentytwo13 import TwentyTwo13Scraper
from .rss_scrapers import NST, FMT, VIBES, BORNEO_POST, SINAR_HARIAN, HARIAN_METRO

SCRAPERS = {
    "malaymail": MalayMailScraper,
    "astroawani": AstroAwaniScraper,
    "sinardaily": SinarDailyScraper,
    "dayakdaily": DayakDailyScraper,
    "twentytwo13": TwentyTwo13Scraper,
    "nst": lambda: NST,
    "fmt": lambda: FMT,
    "thevibes": lambda: VIBES,
    "borneopost": lambda: BORNEO_POST,
    "sinarharian": lambda: SINAR_HARIAN,
    "hmetro": lambda: HARIAN_METRO,
}
