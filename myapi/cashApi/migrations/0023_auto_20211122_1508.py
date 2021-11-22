# Generated by Django 3.2.9 on 2021-11-22 15:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0022_auto_20211122_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='chashback',
        ),
        migrations.AddField(
            model_name='product',
            name='cashback',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 22, 15, 8, 59, 244620)),
        ),
    ]
