import environ
import dj_database_url
from .base import *

DEBUG = False

env = environ.Env()
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

db_from_env = dj_database_url.config()
DATABASES = {
    'default': dj_database_url.config()
}
