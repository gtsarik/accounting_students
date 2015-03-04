"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# email settings
# please, set here you smtp server details and your admin email
DEFAULT_FROM_EMAIL = 'artgrem@gmail.com'

MANAGERS = (
    ('Grigoriy GMAIL', 'artgrem@gmail.com'),
    ('Alexander MailRu', 'favorite.69@mail.ru'),
)

# MANDRILL
ADMIN_EMAIL = 'artgrem@gmail.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'artgrem@gmail.com'
EMAIL_HOST_PASSWORD = 'tsdLAQQ9lAbrvYwn5V8PRA'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# # GMAIL
# ADMIN_EMAIL = 'artgrem@gmail.com'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = '465'
# EMAIL_HOST_USER = 'artgrem@gmail.com'
# EMAIL_HOST_PASSWORD = 'tnoadmxkzabsjcos'
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True

# # MAIL.RU
# ADMIN_EMAIL = 'admin@studentsdb.com'
# EMAIL_HOST = 'imap.mail.ru'
# EMAIL_PORT = '25'
# EMAIL_HOST_USER = 'favorite.69@mail.ru'
# EMAIL_HOST_PASSWORD = 'margo-baby'
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
# # DEFAULT_FROM_EMAIL = 'favorite.69@mail.ru'
# # SERVER_EMAIL = 'favorite.69@mail.ru'

# # LOCALHOST
# ADMIN_EMAIL = 'favorite.69@mail.ru'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '25'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z96e_75vjvc2%cwh+g^#(_5=s87mx!$+a)_*=1%mp-r1hh!k4t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Image Size Variable
IMAGE_SIZE = (1024 ** 2) * 2

# crispy forms style
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'students',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# import sys
# sys.path.insert(0, os.path.join(BASE_DIR, '..'))
from .db import DATABASES

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# TEMPLATE_CONTEXT_PROCESSORS
from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "studentsdb.context_processors.absoluteUrl",
    "studentsdb.context_processors.pagePathTrue",
    "studentsdb.context_processors.listStudent",
    "students.context_processors.groups_processor",
)

PORTAL_URL = 'http://localhost:8000'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
