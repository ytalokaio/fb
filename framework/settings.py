#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
import os
##################################################


'''
    PROJECT DIRS
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


'''
    PROJECT SECRET KEY
'''
SECRET_KEY = 'od1hqq3a^k5qidbity73r!f-_@6*apiif0ni#ni_x$qjwxrock'

'''
    PROJECT DATA FORMAT
'''
DATE_INPUT_FORMATS = ('%d-%m-%Y')

'''
    SET TRUE TO ENABLE DEBUG
'''
DEBUG = True

'''
    SET ADMINS TO ENABLE DEBUG
'''

ADMINS = (
    ('3Y', 'contato@3ysoftwarehouse.com.br'),
)

MANAGERS = ADMINS

'''
    PROJECT HOSTS
'''
ALLOWED_HOSTS = []

'''
    CUSTOM AUTH
'''
AUTH_USER_MODEL = 'default.Usuario'


'''
    APLICATIONS
'''
DJANGO_APPS = [
    'material',
    'material.frontend',
    'material.admin',
    'simple_history',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'smuggler',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    #'debug_toolbar.apps.DebugToolbarConfig',
]
CUSTOM_APPS = [
    'apps.default', 
    
    # SUBCLASS APPS
    'apps.subclasses.empresa.startup',
    'apps.subclasses.usuario.employee',
]
INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS



'''
    MIDDLEWARES
'''
DJANGO_MIDDLEWARES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
]
CUSTOM_MIDDLEWARES = [

]
MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARES + CUSTOM_MIDDLEWARES


'''
    DJANGO CORS
'''
CORS_ORIGIN_ALLOW_ALL = True 


'''
    LOGIN
'''
LOGIN_REDIRECT_URL = '/framework/dashboard/'
LOGIN_URL = '/framework/auth/login/'



'''
    URLS
'''
ROOT_URLCONF = 'framework.urls'



'''
    TEMPLATES
'''
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            'templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                "django.template.context_processors.i18n",
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.media',
                'django.contrib.messages.context_processors.messages',
                'apps.default.context_processors.project_media',
            ],
        },
    },
]


'''
    WSGI
'''
WSGI_APPLICATION = 'framework.wsgi.application'



'''
    DATABASES
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'framework',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': ''
    }
}



'''
    AUTHENTICATION
'''
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


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ]

'''
    INTERNACIONALIZATION
'''
LANGUAGE_CODE = 'pt-br'
LANGUAGES = (
 ('pt-br', ('Brasilian Portuguese')),
 ('en', ('English')),
 ('es', ('Spanish')),
)
LOCALE_PATHS = (
   os.path.join(BASE_DIR, 'locale'),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1


'''
    STATIC FILES
'''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

'''
    UPLOADS MEDIA
'''
MEDIA_URL = '/media/'
