import os
import dj_database_url
from .common import *

DEBUG = False

X_API_TOKEN = os.environ['X_API_TOKEN']

ALLOWED_HOSTS = ['funnyfacts-prod.herokuapp.com']



DATABASES = dj_database_url.config()