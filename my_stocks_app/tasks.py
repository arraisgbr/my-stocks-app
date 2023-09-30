# yourapp/tasks.py
from celery import shared_task
import requests
import os
from stock.models import Stock, StockHistory
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


@shared_task
def get_stock_price(stock_id):

    stock = Stock.objects.get(id=stock_id)

    url_api = os.environ.get('URL_API')
    url_key = os.environ.get('URL_KEY')

    url = f"{url_api}{stock.symbol}&token={url_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        StockHistory.objects.create({
            'price': data['c'],
            'date': datetime.now(),
            'stock': stock,
        })