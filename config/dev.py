from .base import *

DEBUG = True
SECRET_KEY = 'g+_@20^da-#e&y1fxk+^hl^bkp*1!!o)y05bs8cfrv!!5l_v_('

ALLOWED_HOSTS = ['*', 'testserver']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
