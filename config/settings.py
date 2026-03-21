"""
Django settings for config project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / os.getenv("DATABASE_NAME", "db.sqlite3"),
    }
}

# -----------------------
# PASSWORDS
# -----------------------

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

# -----------------------
# I18N
# -----------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

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
