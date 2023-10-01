# your_app/forms.py
from django import forms
from stock.models import Stock


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['symbol', 'min_value', 'max_value', 'frequency', 'wallet']
