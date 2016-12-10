from .settings import *
STATIC_ROOT = '/var/django/www/static'
MEDIA_ROOT = '/var/django/www/media'
DEBUG = False
ADMINS = (
    ('3Y', 'contato@3ysoftwarehouse.com.br'),
)
MANAGERS = ADMINS
ALLOWED_HOSTS = []
SESSION_COOKIE_AGE = 28800
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
'''
    DATABASE CONFIG
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'framework',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': ''
    }
}
'''
    LOG CONFIG
'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

