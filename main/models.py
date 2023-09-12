from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    stock = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
