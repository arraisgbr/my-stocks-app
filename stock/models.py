from django.db import models
from django.contrib.auth.models import User
from utils.verify_email import verify_email
from wallet.models import Wallet


class Stock(models.Model):
    symbol = models.CharField(max_length=8)
    min_value = models.DecimalField(max_digits=8, decimal_places=2)
    max_value = models.DecimalField(max_digits=8, decimal_places=2)
    frequency = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(
        Wallet, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.symbol}"


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
