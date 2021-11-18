from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^cashApi/customer/$', views.CustomerList.as_view(), name='customer-list'),
    url(r'^cashApi/sale/$', views.SaleList.as_view(), name='sale-list'),
    url(r'^cashApi/product/$', views.SaleList.as_view(), name='product-list'),
    ]