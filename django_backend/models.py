from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=False,)
    short_description = models.CharField(max_length=255, null=False,)
    product_description = models.CharField(max_length=512, null=True,)
    stock = models.IntegerField(null=False)
    price = models.DecimalField(null=False)