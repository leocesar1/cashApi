# Generated by Django 3.2.9 on 2021-11-22 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0025_alter_sale_sold_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='cashback',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 15, 18, 55, 251953)),
        ),
    ]
