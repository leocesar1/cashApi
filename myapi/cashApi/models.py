from typing import DefaultDict
from django.db import models
from cpf_field.models import CPFField # import cpf validator

from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import datetime

class Product(models.Model):

    class Meta:
        db_table = 'product'

    def clean(self):
        if self.price > 0:
            return self.price
        else:
            raise ValidationError('O preço do produto não pode ser negativo!')
        
    choices_type = [
        (0, 'A'),
        (1, 'B'),
        (2, 'C')
    ]

    type = models.PositiveSmallIntegerField(
        choices=choices_type,
    )
    price = models.FloatField()
    qty = models.PositiveSmallIntegerField()

    
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

    sold_at = models.DateField(default= datetime.now(),  null=True )
    total = models.FloatField()
    customer = models.TextField(default = '{"name": "", "document": ""}')
    customer_bd = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    products = models.TextField(default = "") 
    products_bd = models.ManyToManyField(Product,) 
    
    def __str__(self):
        template =  "Total sale "+ str(self.total)+" of customer: "#+self.customer_bd.document
        return template