from .settings import *
STATIC_ROOT = '/var/django/www/static'
'''
    DATABASE CONFIG
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'framework',
        'USER': 'root',
        'PASSWORD': 'manohacker',
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

