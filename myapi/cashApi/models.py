from typing import DefaultDict
from django.db import models
from cpf_field.models import CPFField # import cpf validator

from django.core.exceptions import ValidationError
from datetime import datetime

import json

class Product(models.Model):
    # In this class, all products are stored individually,
    # as well as their respective cachebacks in a separate table.
    class Meta:
        db_table = 'product'

    def clean(self):
        # Initial validations
        # Price must not be zero or negative
        if self.price > 0:
            # Values ​​will be rounded
            self.price = round(self.price,2)

            # Errors in cashback validation are performed locally in the function
            if self.cashback == False:
                raise ValidationError('Não foi possível aplicar o programa de cashback neste produto!')
            
            return self
        else:
            raise ValidationError('O preço do produto não pode ser negativo!')

    # Possibilities for the type of product      
    choices_type = [
        ('A', "A"),
        ('B', "B"),
        ('C', "C")
    ]

    type = models.CharField(max_length=1,
        choices=choices_type,
    )

    # Unit price
    price = models.FloatField(default=0.00,)

    # Product quantity
    qty = models.PositiveSmallIntegerField()

    # Cashback amount applied to the product
    cashback = models.FloatField(default=0.00)

    
    def __str__(self):
        return "Product type: " + str(self.type) + ". Qty:  "+ str(self.qty) + " - Price: "+ str(self.price)
        

class Customer(models.Model):
    # In this class, all customers are registered individually, 
    # with a view to future consultations.

    class Meta:
        db_table = 'customers'

    # Document corresponds to the CPF.
    # For validation we have included the CPFField library.
    document = CPFField('cpf', unique=True)

    name = models.CharField(max_length=200)

    def __str__(self):
        return "Customer name: " + self.name + " - Document: "+ self.document
        

class Sale(models.Model):
    # In this class, all ERP requests from the user are received.
    # Once received, the data is treated and separated in the CUSTOMER and PRODUCT tables
    
    class Meta:
        db_table = 'sale'


    sold_at = models.DateTimeField(default= datetime.now(),)
    total = models.FloatField()
    customer = models.JSONField()
    
    # Include customer data in customer database
    customer_bd = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    products = models.JSONField() 
    
    # Include products data in product database
    products_bd = models.ManyToManyField(Product,)
    cashback = models.FloatField(default = 0.00)
    
    def __str__(self):
        data = {
            "document": self.customer_bd.document,
            "cashback": self.cashback
        }
        return json.dumps(data)