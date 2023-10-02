from django.views.generic.detail import DetailView
from app_stock.models import Stock
from app_wallet.models import Wallet
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class WalletDetailView(DetailView):
    model = Wallet
    template_name = 'wallet/pages/wallet_detail.html'
    context_object_name = 'wallet'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        stocks = Stock.objects.all().filter(wallet=self.object)
        context_data['stocks'] = stocks
        return context_data