from .malaymail import MalayMailScraper
from .astroawani import AstroAwaniScraper
from .sinardaily import SinarDailyScraper
from .dayakdaily import DayakDailyScraper
from .twentytwo13 import TwentyTwo13Scraper

SCRAPERS = {
    "malaymail": MalayMailScraper,
    "astroawani": AstroAwaniScraper,
    "sinardaily": SinarDailyScraper,
    "dayakdaily": DayakDailyScraper,
    "twentytwo13": TwentyTwo13Scraper,
}
