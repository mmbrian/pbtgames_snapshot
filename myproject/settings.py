"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd%d!d(25mo7xn$h5y(br%z*%xj28vhf+%2v^5*f(5mzzg2zzo+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

ADMINS = ('Mohsen Mansouryar', 'mohsen.brian@gmail.com')


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'imagekit',
)

CUSTOM_APPS = (
    'myproject.pbtgames_fa',
    'myproject.pbtgames_notif',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'myproject.custom_middleware.LanguageRedirectMiddleware'
)

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pbtgames_db',
        'USER': 'pbtgames_app',
        'PASSWORD': '*PBTGames@MainDATA.Base*',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/media/'

MEDIA_URL = '/uploads/'

# Directories for static assets that aren't tied to a particular app
# app specific static files should be inside a "static" folder inside
# each. for example my_app/static/my_app/myimage.jpg
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "myproject/templates"),
)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = '/home/mmbrian/webapps/pbtgames_static/'
# Absolute path to the directory uploaded files should be collected to.
MEDIA_ROOT = '/home/mmbrian/webapps/pbtgames_uploads/'


EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'pbtgames_tech_mb'
EMAIL_HOST_PASSWORD = '*PBTGames@Technical.Mail3ox*'
DEFAULT_FROM_EMAIL = 'techbot@test.pbtgames.ir'
SERVER_EMAIL = 'techbot@test.pbtgames.ir'

