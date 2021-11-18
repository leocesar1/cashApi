from django.db import models
from cpf_field.models import CPFField # import cpf validator

class Customer(models.Model):
    class Meta:
        db_table = 'customers'

    document = CPFField('cpf')
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Customer name: " + self.name + " - Document: "+ self.document
        

class Sale(models.Model):

    class Meta:
        db_table = 'sale'

    sold_at = models.DateTimeField()
    total = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    products = models.TextField(
        default = "{'type': 0, 'qty': 0, 'value': 0}") 
    
    def __str__(self):
        template =  "Total sale %{total}s of customer: %{customer}s" % {
            'total': self.total,
            'customer': self.customer
        }
        return template.format(self)