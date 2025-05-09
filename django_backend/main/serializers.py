from rest_framework import serializers
from .models import Product

from rest_framework import serializers
from .models import Product, Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['quantity']

class ProductSerializer(serializers.ModelSerializer):
    stock = StockSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'short_description', 'product_description', 'price', 'stock']

    def create(self, validated_data):
        stock_data = validated_data.pop('stock')
        product = Product.objects.create(**validated_data)
        Stock.objects.create(product=product, **stock_data)
        return product

    def update(self, instance, validated_data):
        stock_data = validated_data.pop('stock', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if stock_data:
            Stock.objects.update_or_create(product=instance, defaults=stock_data)
        return instance
