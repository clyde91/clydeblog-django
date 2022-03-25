import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = ")g1ch@o4wi9w$xow5alf1%^zee0pt7%-unw0gu8d0j)satdtkl"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*', ]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clydeblog_db',  # 数据库名称
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


# 邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False   # 是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = True    # 是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.qq.com'   # 发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 465     # 发件箱的SMTP服务器端口
EMAIL_HOST_USER = '66704470@qq.com'    # 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'rysyfshfxfstbhfe'         # 发送邮件的邮箱密码(这里使用的是授权码)
