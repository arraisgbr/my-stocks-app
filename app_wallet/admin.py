from django.contrib import admin

# Register your models here.
from app_wallet.models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    ...