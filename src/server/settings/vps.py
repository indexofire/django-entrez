# -*- coding: utf-8 -*-
import os
from .base import *


DEBUG = os.environ['DEBUG']
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


INSTALLED_APPS += (
    'gunicorn',
    'disqus',
)

LOGIN_REDIRECT_URL = '/account/%(username)s/'
#LOGIN_URL = '/account/login/'
#LOGOUT_URL = '/account/logout/'

LOGIN_URL = '/signin/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login-error/'
LOGOUT_URL = '/logout/'

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