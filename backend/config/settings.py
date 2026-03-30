import os
from pathlib import Path
import dj_database_url

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# SECURITY
# ========================
SECRET_KEY = 'django-insecure-change-this-key'

DEBUG = True

ALLOWED_HOSTS = ['*']


# ========================
# APPLICATIONS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ========================
# URLS & WSGI
# ========================
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# ========================
# DATABASE (PostgreSQL - Render)
# ========================
DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://pmodb_qyve_user:nbvEOzGH0o4Krm3K1A6GbWLReM2tJlzT@dpg-d750vip4tr6s73d1b1ng-a.oregon-postgres.render.com/pmodb_qyve",
        conn_max_age=600,
        ssl_require=True
    )
}


# ========================
# PASSWORD VALIDATION
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


# ========================
# LANGUAGE & TIMEZONE
# ========================
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True


# ========================
# STATIC FILES
# ========================
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# ========================
# DEFAULT PRIMARY KEY
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
