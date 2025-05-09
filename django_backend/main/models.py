from django.db import models

# Create your models here.

class Product(models.Model):
    initial = True

    dependecies = []

    name = models.CharField(max_length=255, null=False,)
    short_description = models.CharField(max_length=255, null=False,)
    product_description = models.TextField(null=True)
    stock = models.IntegerField(null=False)
    price = models.FloatField(null=False)


    def __str__(self):
        return self.name