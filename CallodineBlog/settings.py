"""
Django settings for CallodineBlog project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import datetime

def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    
    return ((delta1 if delta1 > now else delta2) - now).days + 1

ABHI_BDAY = datetime.strptime('May 14 1999', '%b %d %Y')
ABHI_NOD =  calculate_dates(ABHI_BDAY, datetime.now())
AISHU_BDAY = datetime.strptime('Nov 12 1996', '%b %d %Y')
AISHU_NOD =  calculate_dates(AISHU_BDAY, datetime.now())
AKSHU_BDAY = datetime.strptime('Jan 09 1996', '%b %d %Y')
AKSHU_NOD =  calculate_dates(AKSHU_BDAY, datetime.now())
ARAVIND_BDAY = datetime.strptime('Oct 22 1998', '%b %d %Y')
ARAVIND_NOD =  calculate_dates(ARAVIND_BDAY, datetime.now())
OVIYA_BDAY = datetime.strptime('Feb 03 1998', '%b %d %Y')
OVIYA_NOD =  calculate_dates(OVIYA_BDAY, datetime.now())
PRIYA_BDAY = datetime.strptime('Mar 14 1996', '%b %d %Y')
PRIYA_NOD =  calculate_dates(PRIYA_BDAY, datetime.now())
BAJU_BDAY = datetime.strptime('May 27 1999', '%b %d %Y')
BAJU_NOD =  calculate_dates(BAJU_BDAY, datetime.now())
VISWA_BDAY = datetime.strptime('Oct 23 1998', '%b %d %Y')
VISWA_NOD =  calculate_dates(VISWA_BDAY, datetime.now())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hc)7l*k5acl6mm-1d(m=#=1e=we4zdno_3%j6veeqqy=*vw4qu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'microblog.apps.MicroblogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'crispy_bootstrap5',
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

ROOT_URLCONF = 'CallodineBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'users.context_processors.frds_bday',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CallodineBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = 'miniblog'

LOGIN_URL = 'login'

## We have created a MEDIA setting. SO whenever we upload any image now, it'll create the profile_pic directory here in the
## media directory. So our project folder won't get cluttered

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

