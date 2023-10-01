from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Wallet


class WalletDeleteView(DeleteView):
    model = Wallet
    template_name = 'wallet/pages/wallet_detail.html'
    success_url = reverse_lazy('wallet:wallet_list')
