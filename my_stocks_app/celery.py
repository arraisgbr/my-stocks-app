import os
import django
from django.apps import apps
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_stocks_app.settings')

django.setup()

app = Celery('my_stocks_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {}
Stock = apps.get_model('stock', 'Stock')
for stock in Stock.objects.all():
    app.conf.beat_schedule[f'get-stock({stock.id})-price'] = {
        'task': 'my_stocks_app.tasks.get_stock_price',
        'schedule': 10,
        'args': (stock.id,),
    }
