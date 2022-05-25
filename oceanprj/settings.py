"""
Django settings for oceanprj project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(w3an%=5#2wbkhrolxuhpqu^ad6dh&4@ekcf381518qj-$fv-w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['http://185.156.172.76', 'https://oceanfortunes.com','http://www.oceanfortunes.com', 'http://localhost']
CSRF_TRUSTED_ORIGINS = ['http://185.156.172.76','https://oceanfortunes.com','https://www.oceanfortunes.com']

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = ('http://localhost','http://185.156.172.76','https://oceanfortunes.com','https://www.oceanfortunes.com')
# STATIC_URL = 'root/ocean/oceanapp/static/'

# STATIC_ROOT = os.path.join(BASE_DIR,  'staticfiles')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oceanapp',
    'pay',
    'cloudinary',
    'cloudinary_storage',
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

ROOT_URLCONF = 'oceanprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'oceanprj.wsgi.application'


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

LOGIN_URL = 'login'

# MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'oceanfortunes@gmail.com'
EMAIL_HOST_PASSWORD = 'qtfdnxjtfyzggjef'
EMAIL_PORT = 587

# STRIPE_PUBLIC_KEY = "pk_test_51Kfj1uBK9cFspPsyUrQ0N8vmMXnARswBXOmzSOXRTgm39xb3x0JkPSM674jHWNQlxEVdUHE6A2b1eCf39hAV2kas00ATUbgFv4"

# STRIPE_SECRET_KEY = "sk_test_51Kfj1uBK9cFspPsyGF1yiYZegz4qA4oHlIryVf8GtnB7pzw48KJUbDuSs6pDBuseNTgHtkvwYwQ0nIRTLFzrzkmU000OwvBBR"

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'oceans12',
    'API_KEY': '283721882271274',
    'API_SECRET': 'aVVSPuggfThiLcjQZfaFa2vAp0A'
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'