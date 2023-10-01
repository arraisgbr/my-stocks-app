# stock/urls.py
from django.urls import path
from .views import WalletCreateView, WalletDeleteView
from .views import WalletListView, WalletDetailView

app_name = 'wallet'

urlpatterns = [
    path('', WalletListView.as_view(), name='wallet_list'),
    path('<int:pk>/', WalletDetailView.as_view(), name='wallet_detail'),
    path('create/', WalletCreateView.as_view(), name='wallet_create'),
    path('<int:pk>/delete/', WalletDeleteView.as_view(), name='wallet_delete')
]
