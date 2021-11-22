from rest_framework import serializers
from .models import Customer, Sale, Product
from datetime import datetime
import pytz
import requests

def getCashback(typeProduct, totalValue):
    # This function determines the cashback according to the implemented policy
    # Type == "A"  ===>>>> 5%
    # Type == "B"  ===>>>> 10%
    # Type == "C"  ===>>>> 15%
    if typeProduct == "A":
        return round(totalValue*0.05, 2)
    elif typeProduct == "B":
        return round(totalValue*0.1, 2)
    elif typeProduct == "C":
        return round(totalValue*0.15, 2)
    else:
        return False

def senderToApiMT(data):
    return requests.post(
        url = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback',
        data = data
    )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('qty', 'price', 'type')
        
    # Product price must be greater than zero
    def validate_price(self, value):
        if value > 0:
            return value
        raise serializers.ValidationError('Não é possível inserir preços negativos!')

    # The product type must be listed as one of the options
    def validate_type(self, value):
        if value in [c[1] for c in Product.type.field.choices]:
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
        depth = 1

    def validate(self, data):
        """
        Validation of user information
        """
        try:
            jsonCustomer = data['customer']
            customer = Customer.objects.filter(document = jsonCustomer['document'])[0]
            if not customer:
                customer = Customer.objects.create(name = jsonCustomer['name'], document = jsonCustomer['document'])[0]
            data['customer_bd'] = customer
            
        except:
            raise serializers.ValidationError('Falha ao incluir usuário!')

        """
        Validation of products information
        """
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

        """
        Verification of the sum of values
        """
        sum_total = sum(item['qty'] * float(item['value']) for item in jsonProducts)
        if data['total'] == sum_total:
            data['cashback'] = sum(item for item in cashbackSale)
        else:
            raise serializers.ValidationError('O valor total informado está errado!')

        """
        Validation of purchase date.
        """
        if data['sold_at'] > pytz.utc.localize(datetime.now()):
            raise serializers.ValidationError('Não é possível inserir uma compra com data futura.')
        

        """
        Submission to the MaisTodos API
        """
        try:
            data = {'document': customer.document, 'cashback': data['cashback']}
        
            message = senderToApiMT(data)
            print(message)
        except:
            raise serializers.ValidationError('Não foi possível enviar o cashback para a API do MaisTodos.')

        return data
    
