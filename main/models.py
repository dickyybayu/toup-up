from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    available = models.BooleanField()

