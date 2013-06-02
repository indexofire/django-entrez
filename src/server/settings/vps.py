# -*- coding: utf-8 -*-
import os
from .base import *


DEBUG = os.environ['DEBUG']
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = os.environ['SECRET_KEY']
BROKER_URL = os.environ['BROKER_URL']
DISQUS_API_KEY = os.environ['DISQUS_API_KEY']
DISQUS_WEBSITE_SHORTNAME = os.environ['DISQUS_WEBSITE_SHORTNAME']


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
    'disqus',
)

LOGIN_REDIRECT_URL = '/account/%(username)s/'
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
