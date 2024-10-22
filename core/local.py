# settings/local.py

from .base import *
from .cors import *
from .ckeditor import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Локальная база данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
