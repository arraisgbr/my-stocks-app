import json
from django.apps import apps


def create_chart_data(stock):
    StockHistory = apps.get_model('app_stock', 'StockHistory')
    stocks_h = StockHistory.objects.all().filter(stock=stock)
    labels = [stock_h.date.isoformat() for stock_h in stocks_h]
    data = [str(stock_h.price) for stock_h in stocks_h]

    chart_data = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }

    return chart_data
