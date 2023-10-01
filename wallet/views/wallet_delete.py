from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Wallet
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class WalletDeleteView(DeleteView):
    model = Wallet
    template_name = 'wallet/pages/wallet_detail.html'
    success_url = reverse_lazy('wallet:wallet_list')
