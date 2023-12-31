from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    stock = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
