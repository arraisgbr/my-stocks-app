# stock/urls.py
from django.urls import path
from .views import StockListView

app_name = 'stock'

urlpatterns = [
    path('', StockListView.as_view(), name='stock_list'),
]
