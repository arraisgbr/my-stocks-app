from stock.models import Stock
from wallet.models import Wallet
from django import forms


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('symbol', 'min_value', 'max_value', 'frequency', 'wallet')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['wallet'].queryset = Wallet.objects.filter(
            user=user)
