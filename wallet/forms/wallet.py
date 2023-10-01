from ..models import Wallet
from django import forms


class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ('name',)