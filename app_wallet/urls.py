# stock/urls.py
from django.urls import path
from .views import WalletCreateView, WalletDeleteView
from .views import WalletListView, WalletDetailView, WalletListAllView

app_name = 'wallet'

urlpatterns = [
    path('', WalletListAllView.as_view(), name='wallet_list_all'),
    path('<int:pk>/', WalletDetailView.as_view(), name='wallet_detail'),
    path('create/', WalletCreateView.as_view(), name='wallet_create'),
    path('<int:pk>/delete/', WalletDeleteView.as_view(), name='wallet_delete'),
    path('user/', WalletListView.as_view(), name='wallet_list')
]
