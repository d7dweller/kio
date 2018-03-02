#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Khris Byrd'
SITENAME = 'Khris Byrd'
SITEURL = 'http://khris.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('', ''),
#         ('', ''),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/notkhris'),
        ('Twitter', 'https://twitter.com/notkhris'),
        ('LinkedIn', 'https://www.linkedin.com/in/khris-byrd-85aa2852'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "crowsfoot"

## Specifics to pelican-blue theme ###
SIDEBAR_DIGEST = "Linux Admin by day, python coder by night."
MENUITEMS = (('home', '/'),('about', 'about.html'),('projects', 'projects.html'),)

## Specifics to crowsfoot theme ##
GITHUB_ADDRESS = "https://github.com/notkhris"
TWITTER_ADDRESS = "https://twitter.com/notkhris"
SITESUBTITLE = "\"This kid's a nerd. - Seer\""            
