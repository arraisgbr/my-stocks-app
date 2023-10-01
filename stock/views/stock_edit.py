# your_app/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from stock.models import Stock
from stock.forms import StockUpdateForm


class StockUpdateView(UpdateView):
    model = Stock
    form_class = StockUpdateForm
    template_name = 'stock/pages/stock_update.html'
    success_url = reverse_lazy('stock:stock_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
