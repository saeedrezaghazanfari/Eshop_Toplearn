from django.shortcuts import render
from rest_framework import serializers
from eshop_products.models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
