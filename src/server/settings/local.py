# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '../test.db',
    }
}

INSTALLED_APPS += (
    'disqus',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = (
    '127.0.0.1',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

SECRET_KEY = '007'
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
DISQUS_WEBSITE_SHORTNAME = 'djentrez'
