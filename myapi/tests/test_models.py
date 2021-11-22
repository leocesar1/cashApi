from django.test import TestCase
from cashApi.models import Product, Customer, Sale

class CustomerModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Setting up non-modified data for all class methods.")
        Customer.objects.create(name='João', document='123123123-21')
    
    def test_name(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_document(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('document').verbose_name
        self.assertEquals(field_label, 'cpf')

    def setUp(self):
        print("setUp: Running to setup clean data.")
        pass


class ProductModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Setting up non-modified data for all class methods.")
        Product.objects.create(type='A', price= 10.00, qty = 2, cashback = 2.00)

    def test_type_name(self):
        type = Product.objects.get(id=1)
        field_label = type._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type')

    def test_price_name(self):
        price = Product.objects.get(id=1)
        field_label = price._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_qty_name(self):
        qty = Product.objects.get(id=1)
        field_label = qty._meta.get_field('qty').verbose_name
        self.assertEquals(field_label, 'qty')

    def test_cashback_name(self):
        cashback = Product.objects.get(id=1)
        field_label = cashback._meta.get_field('cashback').verbose_name
        self.assertEquals(field_label, 'cashback')

    def test_inclusion_product(self):
        # from django.test.client import Client
        # client = Client()
        response = self.client.get('/cashApi/product')
        print(response.status_code)

    def setUp(self):
        print("setUp: Running to setup clean data.")
        pass
