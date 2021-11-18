from django.db.models.query import QuerySet
from rest_framework import serializers
from .models import Customer, Sale, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False, read_only=False)
    class Meta:
        model = Sale
        fields = '__all__'
        # depth = 1

