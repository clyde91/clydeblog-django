import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clydeblog_db',#数据库名称
        'USER': 'clyde',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# 日志文件
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/clydeblog_debug.log',
        },
        # 'mail_admins': {                         #和邮件有关，有需求就查ysh的40期视频
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        # }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # 'django.request': {
        #     'handlers': ['mail_admins'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
    },
}