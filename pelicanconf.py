#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Andrew'
SITENAME = 'MS Reports'
SITEURL = ''

THEME = 'theme/'
PATH = 'content'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Homepage', 'https://chrizandr.github.io/'),
         ('Github', 'https://github.com/chrizandr/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/chrizandr/'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'data', 'videos', 'pdfs', 'res']
PAGE_EXCLUDES = STATIC_PATHS
ARTICLE_EXCLUDES = STATIC_PATHS
MD_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight, linenums=True)', 'extra', 'tables']
MARKDOWN = {
    'output_format': 'html5',
}

SITEDESCRIPTION = ''

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME = True
DISPLAY_MENU = True
DISPLAY_PAGES_ON_MENU = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
CATEGORIES_URL = 'categories/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL = 'archives/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('All Reports', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
