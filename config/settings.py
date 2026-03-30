"""
Django settings for config project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from celery.schedules import crontab


# -----------------------
# BASE DIR
# -----------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------
# LOAD ENV
# -----------------------

load_dotenv(BASE_DIR / ".env")


# -----------------------
# SECURITY
# -----------------------

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = []

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")


# -----------------------
# REDIS / CELERY
# -----------------------

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"


# -----------------------
# TIMEZONE
# -----------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_TZ = True

USE_I18N = True

CELERY_TIMEZONE = TIME_ZONE


# -----------------------
# APPS
# -----------------------

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_spectacular',
    'django_celery_beat',

    'users',
    'courses',
    'payments',
]

AUTH_USER_MODEL = 'users.User'


# -----------------------
# MIDDLEWARE
# -----------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


# -----------------------
# TEMPLATES
# -----------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# -----------------------
# DATABASE
# -----------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# -----------------------
# PASSWORDS
# -----------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -----------------------
# STATIC
# -----------------------

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -----------------------
# DRF
# -----------------------

REST_FRAMEWORK = {

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}


# -----------------------
# SPECTACULAR
# -----------------------

SPECTACULAR_SETTINGS = {
    "TITLE": "LMS API",
    "DESCRIPTION": "Courses + Payments + Stripe",
    "VERSION": "1.0.0",
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True

CELERY_BEAT_SCHEDULE = {

    "check_users": {

        "task": "users.tasks.deactivate_inactive_users",

        "schedule": crontab(
            minute=0,
            hour=0,
        ),

    },

}
