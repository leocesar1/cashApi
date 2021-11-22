# Generated by Django 3.2.9 on 2021-11-22 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0026_auto_20211122_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 17, 8, 47, 341805)),
        ),
    ]
