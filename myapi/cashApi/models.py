from django.db import models

# first models draft
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
        return "Product type %{type}s - Qty: %{qty}s - Unit Value: %{value}s", {
            'type': self.type,
            'qty': self.qty,
            'value': self.value
        }

class Customer(models.Model):

    class Meta:
        db_table = 'customers'

    document = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return "Customer name %{name}s - document: %{document}s", {
            'name': self.name,
            'document': self.document
        }

class Sale(models.Model):

    class Meta:
        db_table = 'sale'

    total = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    products = models.ManyToManyField(Product, on_delete=models.CASCADE) 
    
    def __str__(self):
        return "Total sale %{total}s of customer: %{customer}s", {
            'total': self.total,
            'customer': self.customer
        }