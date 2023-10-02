from django.contrib import admin

# Register your models here.
from app_stock.models import Stock, StockHistory


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    ...


@admin.register(StockHistory)
class StockHistoryAdmin(admin.ModelAdmin):
    ...