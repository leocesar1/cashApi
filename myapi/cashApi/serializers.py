from rest_framework import serializers
from rest_framework import validators
from .models import Customer, Sale, Product
from datetime import datetime
from rest_framework.validators import UniqueValidator
from json import loads

def getCashback(typeProduct, totalValue):
    if typeProduct == 0:
        return round(totalValue*0.05)
    elif typeProduct == 1:
        return round(totalValue*0.1)
    elif typeProduct == 2:
        return round(totalValue*0.15)
    else:
        return False

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
            jsonCustomer = data['customer']
            customer = Customer.objects.filter(document = jsonCustomer['document'])[0]
            if not customer:
                customer = Customer.objects.create(name = jsonCustomer['name'], document = jsonCustomer['document'])[0]
            data['customer_bd'] = customer
            
        except:
            raise serializers.ValidationError('Falha ao incluir usuário!')

        try:
            jsonProducts = data['products']
            arrayProducts = []
            cashbackSale = []
            for item in jsonProducts:
                product = Product(qty = item['qty'], type = item['type'], price = float(item['value']), cashback = getCashback(typeProduct = item['type'], totalValue = float(item['value']) * item['qty']))
                product.save()
                arrayProducts.append(product.pk)
                cashbackSale.append(product.cashback)
            data['products_bd'] = arrayProducts
        except:
            raise serializers.ValidationError('Falha ao incluir os produtos!')

        sum_total = sum(item['qty'] * float(item['value']) for item in jsonProducts)
        if data['total'] == sum_total:
            data['cashback'] = sum(cashbackSale)
        else:
            raise serializers.ValidationError('O valor total informado está errado!')
        
        # send data to chashback

        return data
    
