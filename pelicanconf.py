#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

PAGINATED_DIRECT_TEMPLATES = ('archives',)
PAGINATION_PATTERNS = ((1, '{base_name}/', '{base_name}/index.html'), (2, '{base_name}/page{number}/', '{base_name}/page{number}/index.html'))

BLOG_START_YEAR = "2015"

COMMENT_SYSTEM_ID = "20774"

ARCHIVES_TITLE = "Archives"
COMMENTS_TITLE = "Comments"
FEED_TITLE = "RSS"
RECENT_POSTS_TITLE = "Recent posts"
SEARCH_TITLE = "Search"
PREV_TITLE = "Prev"
NEXT_TITLE = "Next"
TAG_PAGE_TITLE = "Post tagged by"

AUTHOR = 'Qi Mi'
SITENAME = 'Path of Learning'
SITESUBTITLE = 'discrete, continuous, limit , force'
SITEURL = 'www.pathoflearning.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Other home', 'http://www.pitt.edu/~qim3'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/pittmiqi'),
          ('github', 'http://github.com/pittmiqi'))

DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

STATIC_PATHS = ['images', 'figures', 'downloads', 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

THEME = "pelican-themes\\lazystrap"
#THEME =  "pelican-themes\\lazystrap"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'lightbox', 'tipue_search','liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

#from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.



SITEURL = 'http://pathoflearning.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GITHUB_USERNAME = "pittmiqi"
DISQUS_SITENAME = "pathoflearning"
GOOGLE_ANALYTICS = "UA-69748436-1"
