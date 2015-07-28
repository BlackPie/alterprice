from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

module = os.environ.get('DJANGO_SETTINGS_MODULE')
if not module:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from configurations import importer
importer.install()

app = Celery('alterprice')

CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_REDIRECT_STDOUTS_LEVEL = 'INFO'

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
