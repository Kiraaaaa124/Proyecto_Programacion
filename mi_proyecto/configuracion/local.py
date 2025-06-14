from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Proyecto',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost', 
        'PORT': '5432',     
    }
}

STATIC_URL = 'static/'
