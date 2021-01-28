import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')g1ch@o4wi9w$xow5alf1%^zee0pt7%-unw0gu8d0j)satdtkl'
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clydeblog_db',#数据库名称
        'USER': 'clyde',
        'PASSWORD': 'yitian3314',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
