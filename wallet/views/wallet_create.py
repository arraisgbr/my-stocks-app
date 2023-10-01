from django.views.generic.edit import FormView
from wallet.forms import WalletForm
from django.urls import reverse_lazy


class WalletCreateView(FormView):
    template_name = 'wallet/pages/wallet_create.html'
    form_class = WalletForm
    success_url = reverse_lazy('wallet:wallet_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)