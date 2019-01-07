#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Andrew'
SITENAME = 'MS Reports'
SITEURL = ''

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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'data']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables':{},
    }
}

