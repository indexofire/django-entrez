# -*- coding: utf-8 -*-
import os
import json
import djcelery
from django.core.exceptions import ImproperlyConfigured

djcelery.setup_loader()

DEBUG = os.environ['DEBUG']
TEMPLATE_DEBUG = DEBUG
DATABASES = os.environ['DATABASE_URL']


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ADMINS = ()
MANAGERS = ADMINS
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'

ROOT_URLCONF = 'server.urls'
WSGI_APPLICATION = 'server.wsgi.application'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'entrez',
    'south',
    'djcelery',
    'userena',
    'guardian',
    'easy_thumbnails',
    'account',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

if DEBUG:
    INSTALLED_APPS += (
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
    BROKER_URL = 'redis://localhost:6379/0'
else:
    SECRET_KEY = os.environ['SECRET_KEY']
    BROKER_URL = 'redis://localhost:6379/0'

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE = 'account.UserProfile'
LOGIN_REDIRECT_URL = '/account/%(username)s/'
LOGIN_URL = '/account/signin/'
LOGOUT_URL = '/account/signout/'

USERENA_MUGSHOT_GRAVATAR = True
USERENA_SIGNIN_REDIRECT_URL = '/account/%(username)s/'

if DEBUG:
    USERENA_ACTIVATION_REQUIRED = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
