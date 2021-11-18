from django.db import models
from cpf_field.models import CPFField # import cpf validator

class Product(models.Model):

    class Meta:
        db_table = 'product'

    choices_type = [
        (0, 'A'),
        (1, 'B'),
        (2, 'C')
    ]

    type = models.PositiveSmallIntegerField(
        choices=choices_type,
    )
    value = models.FloatField()
    qty = models.PositiveSmallIntegerField()

    def __str__(self):
        return "Product type: " + str(self.type) + ". Qty:  "+ str(self.qty) + " - Value: "+ str(self.value)
        

class Customer(models.Model):
    class Meta:
        db_table = 'customers'

    document = CPFField('cpf')
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not Customer.objects.filter(document = self.document):
            super().save(*args, **kwargs)
        else:
            pass

    def __str__(self):
        return "Customer name: " + self.name + " - Document: "+ self.document
        

class Sale(models.Model):

    class Meta:
        db_table = 'sale'

    sold_at = models.DateTimeField()
    total = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product,) 
    
    def __str__(self):
        template =  "Total sale %{total}s of customer: %{customer}s" % {
            'total': self.total,
            'customer': self.customer
        }
        return template.format(self)