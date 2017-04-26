'''
A production settings for heroku.com
'''

from .common import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'gunicorn',
)

DATABASES['default'] = dj_database_url.config()
SECRET_KEY = env('DJANGO_SECRET_KEY')
# Honor the 'X-Forwarded-Proto' SECURE_PROXY_SSL_HEADERer for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)

# ---------------------------------- CORS settings ------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
