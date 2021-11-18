# Generated by Django 3.2.9 on 2021-11-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0006_auto_20211118_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='products',
        ),
        migrations.AddField(
            model_name='sale',
            name='products',
            field=models.ManyToManyField(to='cashApi.Product'),
        ),
    ]
