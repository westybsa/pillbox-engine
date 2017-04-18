from __future__ import absolute_import, unicode_literals
import os
import sys
from celery import Celery

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(BASE_DIR + '/pillbox-engine')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engine.config.production')

app = Celery('pillbox')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

