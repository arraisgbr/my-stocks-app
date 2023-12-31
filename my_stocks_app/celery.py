import os
import django
from django.apps import apps
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_stocks_app.settings')

django.setup()

app = Celery('my_stocks_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {}
Stock = apps.get_model('app_stock', 'Stock')
for stock in Stock.objects.all():
    app.conf.beat_schedule[f'get-stock({stock.id})-price'] = {
        'task': 'my_stocks_app.tasks.get_stock_price',
        'schedule': crontab(minute=f"*/{stock.frequency}"),
        'args': (stock.id,),
    }
