# -*- coding: utf-8 -*-
# Django settings for a Codespeed project.
import os

DEBUG = True

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.split(BASEDIR)[1]

#: The directory which should contain checked out source repositories:
REPOSITORY_BASE_PATH = os.path.join(BASEDIR, "repos")

ADMINS = (
    ('Leon Evers', 'leon@millcomputing.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASEDIR, 'data.db'),
    }
}

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

MEDIA_ROOT = os.path.join(BASEDIR, "media")

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

SECRET_KEY = 'as%n_m#)^vee2pe91^^@c))sl7^c6t-9r8n)_69%)2yt+(la2&'

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = '{0}.urls'.format(TOPDIR)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASEDIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'codespeed',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASEDIR, "sitestatic")
STATICFILES_DIRS = (
    os.path.join(BASEDIR, 'static'),
)

# Codespeed settings that can be overwritten here.
from codespeed.settings import *

DEF_BRANCH = "default"
CHART_ORIENTATION = "horizontal"
USE_MEDIAN_BANDS = True
COMP_EXECUTABLES = [
    ('cycles', 'nosimd'),
    ('cycles', 'L'),
]
DEF_BENCHMARK = 'coremark'

ALLOWED_HOSTS = [
    u'y.millcomputing.com',  # Allow domain and subdomains
    u's11.millcomputing.com',
    '127.0.0.1',
    'localhost',
    'mill-22-4',
]
WEBSITE_NAME = "Mill Speed Site"  # This name will be used in the reports RSS feed
