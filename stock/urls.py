# stock/urls.py
from django.urls import path
from .views import StockListView
from .views import StockDetailView

app_name = 'stock'

urlpatterns = [
    path('', StockListView.as_view(), name='stock_list'),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail')
]
