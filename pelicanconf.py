import datetime
import os

AUTHOR = "sfiera"
SITENAME = os.environ.get("SITENAME", "cassette.vision")
SITEURL = ""
REPO = "https://github.com/sfiera/cassette.vision"

RELPATH = {
    "cassette.vision": "content/cv",
    "super.cassette.vision": "content/scv",
    "pocket.cassette.vision": "content/pcv",
}[SITENAME]
PATH = RELPATH

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
MENUITEMS = []


IGNORE_FILES = [".*", "*.rsti"]
LINKS = []
SOCIAL = []
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NOW = datetime.datetime.now()
