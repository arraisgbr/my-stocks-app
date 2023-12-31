from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"