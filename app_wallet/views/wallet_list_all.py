from django.views.generic.list import ListView
from app_wallet.models import Wallet
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class WalletListAllView(ListView):
    model = Wallet
    template_name = 'wallet/pages/wallet_list_all.html'
    context_object_name = 'wallets'
    paginate_by = 10