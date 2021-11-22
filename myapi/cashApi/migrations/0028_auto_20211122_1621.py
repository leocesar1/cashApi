# Generated by Django 3.2.9 on 2021-11-22 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0027_auto_20211122_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='customer',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='sale',
            name='products',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sold_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 21, 47, 19119)),
        ),
    ]
