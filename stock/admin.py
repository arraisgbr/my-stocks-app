from django.contrib import admin

# Register your models here.
from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    ...