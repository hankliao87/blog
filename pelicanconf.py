#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'hankliao87'
SITENAME = u'Hank Liao\'s Blog'
# SITESUBTITLE = 'A personal blog.'
SITEURL = ''
THEME = 'theme'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = 'en'
PATH = 'content'
LOGO_IMG = 'images/logo.png'
REPO_NAME = 'hankliao87/blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_URL = 'https://github.com/hankliao87/'
# TWITTER_URL = '/'
# FACEBOOK_URL = '/'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# path-specific metadata
EXTRA_PATH_METADATA = {}

# static paths will be copied without parsing their contents
STATIC_PATHS = ['images']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

TIPUE_SEARCH= True

PLUGIN_PATHS = ['plugins']
PLUGINS = ["render_math", "tag_cloud", "better_codeblock_line_numbering", "pelican-encrypt-content", "tipue_search"]
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

MARKDOWN = {
    'extensions' : ['markdown.extensions.codehilite', 'markdown.extensions.extra', 'mdx_include', 'markdown.extensions.admonition'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': 'False'},
    },
}
TAG_CLOUD_STEPS = 4

ARTICLE_PATHS = ['articles']
ARTICLE_EXCLUDES = []
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DRAFT_URL = 'posts/draft/{slug}/'
DRAFT_SAVE_AS = 'posts/draft/{slug}/index.html'

MENUITEMS = (
  ('Home','/'),
  ('About','/about.html'),
#   ('Contact','/contact/'),
  ('Blog','/blog/'),
)

# SUMMARY_MAX_LENGTH = 20

DATE_FORMATS = {
    'en': ('%Y/%m/%d'),
}

