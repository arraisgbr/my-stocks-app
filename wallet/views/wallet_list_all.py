from django.views.generic.list import ListView
from wallet.models import Wallet


class WalletListAllView(ListView):
    model = Wallet
    template_name = 'wallet/pages/wallet_list_all.html'
    context_object_name = 'wallets'
    paginate_by = 10