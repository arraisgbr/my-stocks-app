# your_app/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from app_stock.models import Stock
from app_stock.forms import StockUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockUpdateForm
    template_name = 'stock/pages/stock_update.html'
    success_url = reverse_lazy('stock:stock_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
