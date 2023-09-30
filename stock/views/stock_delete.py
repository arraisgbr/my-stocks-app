from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Stock


class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'stock/pages/stock_detail.html'
    success_url = reverse_lazy('stock:stock_list')
