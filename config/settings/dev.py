# config/settings/dev.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Opcional: configuración para emails en consola, logging, etc.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
