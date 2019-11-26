from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from sandbox import settings_dev

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sandbox.settings_dev')

app = Celery('sandbox', broker=settings_dev.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(settings_dev.INSTALLED_APPS)

if __name__ == '__main__':
    app.start()
