from django.views.generic.list import ListView
from app_stock.models import Stock
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class StockListView(ListView):
    model = Stock
    template_name = 'stock/pages/stock_list.html'
    context_object_name = 'stocks'
    paginate_by = 10

    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)