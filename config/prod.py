import dj_database_url
from .base import *

DEBUG = False

# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'hrcwn098',
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }

db_from_env = dj_database_url.config()
DATABASES = {
    'default': dj_database_url.config()
}
