# Generated by Django 3.2.9 on 2021-11-22 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0016_alter_sale_sold_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sold_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 14, 11, 56, 902484)),
        ),
    ]