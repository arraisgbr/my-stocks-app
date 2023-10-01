from django.views.generic.list import ListView
from wallet.models import Wallet
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class WalletListView(ListView):
    model = Wallet
    template_name = 'wallet/pages/wallet_list.html'
    context_object_name = 'wallets'
    paginate_by = 10

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)