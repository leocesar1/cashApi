from django.contrib import admin
from .models import Customer, Product, Sale
from django import forms
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'value', 'qty')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'document')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id','customer', 
    # 'products'
    )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Product, ProductAdmin)