from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    short_description = models.CharField(max_length=255, null=False)
    product_description = models.TextField(null=True)
    price = models.FloatField(null=False)
    image = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in stock"
