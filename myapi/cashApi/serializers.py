from rest_framework import serializers
from rest_framework import validators
from .models import Customer, Sale, Product
from datetime import datetime
from rest_framework.validators import UniqueValidator
from json import loads


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('qty', 'price', 'type')

    def validate_price(self, value):
        if value > 0:
            return value
        raise serializers.ValidationError('Não é possível inserir preços negativos!')

    def validate_type(self, value):
        if value >= 0 and value < 3:
            return value
        raise serializers.ValidationError('Tipo de produto não cadastrado!')
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = 'customer', 'products', 'sold_at', 'total'
        # depth = 1

    def validate(self, data):
        try:
            jsonCustomer = loads(data['customer'])
            customer = Customer.objects.filter(document = jsonCustomer['document'])[0]
            if not customer:
                customer = Customer.objects.create(name = jsonCustomer['name'], document = jsonCustomer['document'])[0]
            data['customer_bd'] = customer
            
        except:
            raise serializers.ValidationError('Falha ao incluir usuário!')

        try:
            jsonProducts = loads(data['products'])
            arrayProducts = []
            for item in jsonProducts:
                product = Product(qty = item['qty'], type = item['type'], price = item['price'])
                product.save()
                arrayProducts.append(product.pk)
            data['products_bd'] = arrayProducts
        except:
            raise serializers.ValidationError('Falha ao incluir os produtos!')

        sum_total = sum(item['qty'] * item['price'] for item in jsonProducts)
        if data['total'] == sum_total:
            pass
        else:
            raise serializers.ValidationError('O valor total informado está errado!')
        
        return data
    
