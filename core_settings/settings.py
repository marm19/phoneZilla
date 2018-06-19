# coding=utf-8
"""
Django settings for core_settings project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .theme_config import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6*%a46qs(&4fgsh5@3zti_9*sd#dw%lg4s-rhy^&udd%%*-i4r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'main.apps.SuitConfig',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'main',
    'inventory_management',
    'sale_record',
    'rest_framework',
    'rest_framework.authtoken',
    'djmoney',
    'nested_inline',
    'easy_select2',
    'phonenumber_field',
    # 'import_export',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Rest Framework global configuration for project
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

ROOT_URLCONF = 'core_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'inventory_management.context_processors.site_details',
            ],
        },
    },
]

WSGI_APPLICATION = 'core_settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Selenium Test
CHROME_DRIVER_PATH = r"F:\dev\_selenium\ChromeDriver\chromedriver.exe"

LOGIN_REDIRECT_URL = 'home'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
MEDIA_URL = '/files/'
MEDIA_ROOT = os.path.join(BASE_DIR, "user_files")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# STATIC_ROOT = '/assets/'
# STATIC_ROOT_DIR = os.path.join(BASE_DIR, 'assets')

# File upload handlers
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # in bytes

# Module Setting
# Below Include Module details which you want to change
PHONENUMBER_DEFAULT_REGION = "IN"
PRODUCT_MAKER = {
    "Book": ("Publisher", "Launched"),
    "Groceries": ("Supplier", "Manufactured"),
    "Software": ("Developer", "Released"),
    "Pharmacy": ("Distributor", "Launched"),
    "Electronics": ("Manufacturer", "Launched"),
    "Mobile": ("Manufacturer", "Launched")
}  # Product type may be book, software a specific hardware, groceries etc.
PRODUCT_TYPE = "Mobile"
COMPANY_TITLE = "PhoneZilla"  # Title of your company
COMPANY_LOGO = "http://icons.iconarchive.com/icons/graphicloads/100-flat-2/256/mobile-2-icon.png"
COPYRIGHT_SINCE = 2018
COMPANY_EMAIL = "company@example.com"
COMPANY_CONTACT_NUMBER = "+91 99991 99991"
COMPANY_WEBSITE = ""
COMPANY_ADDRESS_LINE_ONE = "Shop No. 5, R World 21,Sector-21"
COMPANY_ADDRESS_LINE_TWO = "Gandhinagar, Gujarat-382021"
COMPANY_COUNTRY = "India"

# Invoice Config
INV_ROOT = os.path.join(MEDIA_ROOT, "invoices")
if not os.path.exists(INV_ROOT):
    os.makedirs(INV_ROOT)
# INV_LOGO = "http://icons.iconarchive.com/icons/graphicloads/100-flat-2/256/mobile-2-icon.png"  # Web Path
INV_LOGO = os.path.join(STATICFILES_DIRS[0], "assets", "logos", "mobile-icon.png")
INV_CURRENCY_SYMBOL = "₹"
INV_CURRENCY_PREFIX = "INR"
INV_CURRENCY = "Indian Rupees"
GST_NUMBER = "00000000"
