# -*- coding: utf-8 -*-
import os
from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = os.environ['SECRET_KEY']
BROKER_URL = os.environ['BROKER_URL']
DISQUS_API_KEY = os.environ['DISQUS_API_KEY']
DISQUS_WEBSITE_SHORTNAME = os.environ['DISQUS_WEBSITE_SHORTNAME']

ALLOWED_HOSTS = [
    '.django-entrez.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-entrez',
        'USER': 'mark',
        'PASSWORD': os.environ["DATABASE_PWD"],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:1",
        "OPTIONS": {
        "CLIENT_CLASS": "redis_cache.client.DefaultClient",
        }
    }
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

INSTALLED_APPS += (
    'gunicorn',
    'disqus',
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['EMAIL_ADDRESS']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PWD']
EMAIL_USE_TLS = True

FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
FACEBOOK_API_SECRET = os.environ['FACEBOOK_API_SECRET']
TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
GOOGLE_OAUTH2_CLIENT_ID = os.environ['GOOGLE_OAUTH2_CLIENT_ID']
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']
WEIBO_CLIENT_KEY = os.environ['WEIBO_CLIENT_KEY']
WEIBO_CLIENT_SECRET = os.environ['WEIBO_CLIENT_SECRET']
