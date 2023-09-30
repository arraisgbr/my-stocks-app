from django.views.generic.detail import DetailView
from stock.models import Stock


class StockDetailView(DetailView):
    model = Stock
    template_name = 'stock/pages/stock_detail.html'
    context_object_name = 'stock'