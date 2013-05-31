# -*- coding: utf-8 -*-
from .base import *


DEBUG = os.environ['DEBUG']
TEMPLATE_DEBUG = DEBUG
DATABASES = os.environ['DATABASE_URL']
SECRET_KEY = os.environ['SECRET_KEY']
BROKER_URL = os.environ['BROKER_URL']
