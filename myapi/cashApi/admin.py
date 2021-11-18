from django.contrib import admin
from .models import Customer, Sale
from django import forms
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'document')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id',
     'customer', 
     'products')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale, SaleAdmin)