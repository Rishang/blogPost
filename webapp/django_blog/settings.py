"""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Declare env vars
STATE = os.environ.get("STAGE")
env = environ.Env(DJANGO_DEBUG_MODE=(bool, True))

# Reading .env file
if os.environ.get("STAGE") == "TESTING":
    env_file = os.path.join(BASE_DIR, ".env.dev")
    environ.Env.read_env(env_file)

if os.environ.get("STAGE") == "PRODUCTION":
    env = environ.Env(
        DJANGO_SECRET_KEY   = (str, os.environ.get("DJANGO_SECRET_KEY")),
        DJANGO_ALLOWED_HOST = (str, os.environ.get("DJANGO_ALLOWED_HOST")),
        DJANGO_DEBUG_MODE   = (bool, os.environ.get("DJANGO_DEBUG_MODE")),
        POSTGRES_DB         = (str, os.environ.get("POSTGRES_DB")),
        POSTGRES_USER       = (str, os.environ.get("POSTGRES_USER")),
        POSTGRES_PASSWORD   = (str, os.environ.get("POSTGRES_PASSWORD")),
        POSTGRES_HOSTNAME   = (str, os.environ.get("POSTGRES_HOSTNAME")),
        DATABASE_PORT       = (int, os.environ.get("DATABASE_PORT")),
    )
else:
    env_file = os.path.join(BASE_DIR, ".env.local")
    environ.Env.read_env(env_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(env.bool("DJANGO_DEBUG_MODE")))

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOST").split(',')

CSRF_TRUSTED_ORIGINS = ['https://*.preview.app.github.dev']

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig', 
    'register.apps.RegisterConfig',
    
    'django_extensions',
    'widget_tweaks',
    'sorl.thumbnail',
    'taggit',
    'storages',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'django_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/' + 'db.sqlite3',
    },
}

try:
    postgres = {
        'ENGINE': env("DATABASE_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("POSTGRES_HOSTNAME"),
        'PORT': env("DATABASE_PORT"),
    }
    DATABASES["default"] = postgres

except:
    print(f"INFO: Using \"default\" Database, Postgres-SQL not configed in {env_file}.")

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = BASE_DIR + '/assets/'
STATIC_URL = '/static/'

MEDIA_ROOT = BASE_DIR + '/media/'
MEDIA_URL = '/media/'
X_FRAME_OPTIONS = 'SAMEORIGIN'
THUMBNAIL_PREFIX = 'compressed_images/'
# SESSION_COOKIE_HTTPONLY = False


if STATE == "PRODUCTION":
    
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_FILE_OVERWRITE = True
    AWS_DEFAULT_ACL = None
