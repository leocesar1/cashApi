# Generated by Django 3.2.9 on 2021-11-19 17:01

import cpf_field.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0008_rename_value_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='document',
            field=cpf_field.models.CPFField(max_length=14, unique=True, verbose_name='cpf'),
        ),
    ]