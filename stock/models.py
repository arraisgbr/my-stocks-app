from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(max_length=8)
    min_value = models.DecimalField(max_digits=8, decimal_places=2)
    max_value = models.DecimalField(max_digits=8, decimal_places=2)
    frequency = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.symbol}"