import os
import dj_database_url
from .common import *

DEBUG = False

X_API_TOKEN = os.environ['X_API_TOKEN']

ALLOWED_HOSTS = ['funnyfactsapp-prod.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}