from django.contrib import admin

# Register your models here.
from .models import Stock, StockHistory


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    ...


@admin.register(StockHistory)
class StockHistoryAdmin(admin.ModelAdmin):
    ...