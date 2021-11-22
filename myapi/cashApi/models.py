from typing import DefaultDict
from django.db import models
from cpf_field.models import CPFField # import cpf validator

from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import datetime

import json

class Product(models.Model):

    class Meta:
        db_table = 'product'

    def clean(self):
        if self.price > 0:
            self.price = round(self.price,2)
            if self.cashback == False:
                raise ValidationError('Não foi possível aplicar o programa de cashback neste produto!')
            else:
                self.cashback = round(self.cashback,2)
            return self
        else:
            raise ValidationError('O preço do produto não pode ser negativo!')

        
        
    choices_type = [
        ('A', "A"),
        ('B', "B"),
        ('C', "C")
    ]

    type = models.CharField(max_length=1,
        choices=choices_type,
    )
    price = models.FloatField(default=0.00,)
    qty = models.PositiveSmallIntegerField()
    cashback = models.FloatField(default=0.00)

    
    def __str__(self):
        return "Product type: " + str(self.type) + ". Qty:  "+ str(self.qty) + " - Price: "+ str(self.price)
        

class Customer(models.Model):
    class Meta:
        db_table = 'customers'

    document = CPFField('cpf', unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Customer name: " + self.name + " - Document: "+ self.document
        

class Sale(models.Model):

    class Meta:
        db_table = 'sale'

    sold_at = models.DateField(default= datetime.now())
    total = models.FloatField()
    customer = models.JSONField(default = {"name": "", "document": ""})
    customer_bd = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    products = models.JSONField(default = "") 
    products_bd = models.ManyToManyField(Product,)
    cashback = models.FloatField(default = 0.00)
    
    def __str__(self):
        data = {
            "document": self.customer_bd.document,
            "cashback": self.cashback
        }
        return json.dumps(data)