from django.views.generic.edit import FormView
from stock.forms import StockForm
from django.urls import reverse_lazy


class StockCreateView(FormView):
    template_name = 'stock/pages/stock_create.html'
    form_class = StockForm
    success_url = reverse_lazy('stock:stock_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)