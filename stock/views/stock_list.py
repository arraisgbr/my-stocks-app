from django.views.generic.list import ListView
from stock.models import Stock


class StockListView(ListView):
    model = Stock
    template_name = 'stock/pages/stock_list.html'
    context_object_name = 'stocks'
    paginate_by = 10

    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)