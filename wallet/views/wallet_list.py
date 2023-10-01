from django.views.generic.list import ListView
from wallet.models import Wallet


class WalletListView(ListView):
    model = Wallet
    template_name = 'wallet/pages/wallet_list.html'
    context_object_name = 'wallets'
    paginate_by = 10

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)