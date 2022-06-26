import os
from .common import *

DEBUG = True

X_API_KEY = os.environ['X_API_TOKEN']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'funnyfactsdb',
        'HOST': 'mysql',
        # 'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Qwerty1234'
    }
}

