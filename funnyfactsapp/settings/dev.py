from .common import *

DEBUG = True

X_API_TOKEN = "SECRET_API_KEY"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'funnyfactsdb',
        'HOST': 'mysql', #localhost
        'USER': 'root',
        'PASSWORD': 'Qwerty1234'
    }
}

