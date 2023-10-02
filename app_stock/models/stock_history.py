from django.db import models
from utils.verify_email import verify_email
from app_stock.views import Stock


class StockHistory(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        stock = self.stock
        user = stock.user
        verify_email(self, stock, user)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.stock} with price {self.price} at {self.date}"