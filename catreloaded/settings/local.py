from .common import *


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'catreloaded',
        'USER': 'postgres',
        'HOST': 'localhost',
        'ATOMIC_REQUESTS': True,
    }
}

INSTALLED_APPS += [
    'django_extensions',
]
