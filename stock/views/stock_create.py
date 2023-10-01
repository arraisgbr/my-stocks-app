from django.views.generic.edit import FormView
from stock.forms import StockForm
from django.urls import reverse_lazy


class StockCreateView(FormView):
    template_name = 'stock/pages/stock_create.html'
    form_class = StockForm
    success_url = reverse_lazy('stock:stock_list')

    def form_valid(self, form):
        stock = form.save(commit=False)
        stock.user = self.request.user
        stock.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
