"""
Django settings for satudata_project project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from .secret import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = secret_debug

ALLOWED_HOSTS = secret_allowed_host


# Application definition

INSTALLED_APPS = [
    # Admin Interface
    'admin_interface',
    'colorfield',

    # Array and Dictionary
    'django_better_admin_arrayfield',
    'django_admin_hstore_widget',

    # Native Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.gis',

    # Imported Apps
    'crispy_forms',
    'crispy_bootstrap5',
    'leaflet',
    'import_export',
    'django_user_agents',

    # Created Apps
    'data',
    'operation',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # ADDDED MIDDLEWARE
    'django_user_agents.middleware.UserAgentMiddleware',
]

MIDDLEWARE_CLASSES = (
    # other middlewares...
    'django_user_agents.middleware.UserAgentMiddleware',
)

ROOT_URLCONF = 'satudata_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # CUSTOM CONTEXT PROCESSOR
                'operation.context_processors.profil',
            ],
        },
    },
]

WSGI_APPLICATION = 'satudata_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }

    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': secret_name,
        'USER': secret_user,
        'PASSWORD': secret_password,
        'HOST': secret_host,
        'PORT': secret_port,
    }
}


# Password validation
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

# Login authentication
AUTHENTICATION_BACKENDS = ['satudata_project.authentications.EmailBackend']

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# Login System
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'site/public/static')
else:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'site/public/static/'),
    )

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'site/public/media')

# DJANGO EMAIL
EMAIL_BACKEND = email_backend
EMAIL_HOST = email_host
EMAIL_PORT = email_port
EMAIL_USE_TLS = email_use_tls
EMAIL_HOST_USER = email_user
EMAIL_HOST_PASSWORD = email_password

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Admin Interface
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Django Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# GDAL for Testing in Windows
if os.name == 'nt':
    OSGEO4W = r"C:\OSGeo4W"
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
    GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal307.dll'
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

# LEAFLET
LEAFLET_CONFIG = {
    'DEFAULT_CENTER' : (-3, 118),
    'DEFAULT_ZOOM' : 5,
    'MAX_ZOOM' : 18,
    'MIN_ZOOM' : 3,
    'SCALE' : 'metric',
    'RESET_VIEW': False,
    'ATTRIBUTION_PREFIX' : 'Kaleka Satu Data | Leaflet',
    
    'PLUGINS': {
        'forms': {
            'auto-include': True
        },
        'fullscreen': {
            'css': ['/static/leaflet/geolocation/L.Control.Locate.min.css'],
            'js': ['/static/leaflet/geolocation/L.Control.Locate.min.js'],
            'auto-include': True
        }
    },

    'TILES': [
        ('OpenStreetMap', 'https://tile.openstreetmap.org/{z}/{x}/{y}.png', {'attribution': ' © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}),
        ('ESRI Imagery', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {'attribution': '© <a href="https://www.arcgis.com/">Esri</a>, Maxar, Earthstar Geographics, and the GIS User Community'})
    ],
}

# GOOGLE CLOUD STORAGE
from google.oauth2 import service_account

DEFAULT_FILE_STORAGE = secret_storage_default
GS_BUCKET_NAME = secret_storage_bucket
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(secret_storage_credential)
