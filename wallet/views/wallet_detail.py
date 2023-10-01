from django.views.generic.detail import DetailView
from stock.models import Stock
from wallet.models import Wallet


class WalletDetailView(DetailView):
    model = Wallet
    template_name = 'wallet/pages/wallet_detail.html'
    context_object_name = 'wallet'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        stocks = Stock.objects.all().filter(wallet=self.object)
        context_data['stocks'] = stocks
        return super().get_context_data(**kwargs)