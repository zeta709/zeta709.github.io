#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'zeta709'
SITENAME = u'zeta709'
SITEURL = ''

TIMEZONE = 'Asia/Seoul'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
DEFAULT_DATE = 'fs'

DEFAULT_LANG = u'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Themes
GITHUB_URL = "https://github.com/zeta709"

PLUGINS = [
    'pelican_gist',
]
