# stock/urls.py
from django.urls import path
from app_stock.views import StockListView, StockDetailView
from app_stock.views import StockCreateView, StockDeleteView, StockUpdateView

app_name = 'stock'

urlpatterns = [
    path('', StockListView.as_view(), name='stock_list'),
    path('<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
    path('create/', StockCreateView.as_view(), name='stock_create'),
    path('<int:pk>/delete/', StockDeleteView.as_view(), name='stock_delete'),
    path('update/<int:pk>', StockUpdateView.as_view(), name='stock_update')
]
