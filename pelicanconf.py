import datetime
import os

AUTHOR = "sfiera"
SITENAME = os.environ.get("SITENAME", "cassette.vision")
SITEURL = ""
REPO = "https://github.com/sfiera/cassette.vision"

PATH = {
    "cassette.vision": "content/cv",
    "super.cassette.vision": "content/scv",
    "pocket.cassette.vision": "content/pcv",
}[SITENAME]

THEME = "theme"

TIMEZONE = "Asia/Tokyo"

PAGE_PATHS = [""]
PAGE_URL = "{slug}"
PAGE_SAVE_AS = PAGE_URL + ".html"

STATIC_PATHS = [""]
STATIC_URL = "{path}"
STATIC_SAVE_AS = "{path}"

DIRECT_TEMPLATES = []
ARTICLE_PATHS = []

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = {
    "cassette.vision": [
        ("Super Cassette Vision", "https://super.cassette.vision/"),
        ("Game Pocket Computer", "https://pocket.cassette.vision/"),
        ("Titles", "title"),
    ],
    "super.cassette.vision": [
        ("Cassette Vision", "https://cassette.vision/"),
        ("Game Pocket Computer", "https://pocket.cassette.vision/"),
        ("Titles", "title"),
    ],
    "pocket.cassette.vision": [
        ("Cassette Vision", "https://cassette.vision/"),
        ("Super Cassette Vision", "https://super.cassette.vision/"),
        ("Titles", "title"),
    ],
}[SITENAME]


IGNORE_FILES = [".*", "*.rsti"]
LINKS = []
SOCIAL = []
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NOW = datetime.datetime.now()
