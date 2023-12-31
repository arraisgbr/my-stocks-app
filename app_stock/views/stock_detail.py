from django.views.generic.detail import DetailView
from app_stock.models import Stock
from utils import create_chart_data
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class StockDetailView(DetailView):
    model = Stock
    template_name = 'stock/pages/stock_detail.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        chart_data = create_chart_data(self.object)
        context_data['chart_data'] = chart_data
        return context_data
