from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Stock
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class StockDeleteView(DeleteView):
    model = Stock
    template_name = 'stock/pages/stock_detail.html'
    success_url = reverse_lazy('stock:stock_list')
