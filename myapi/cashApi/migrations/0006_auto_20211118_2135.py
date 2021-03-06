# Generated by Django 3.2.9 on 2021-11-18 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashApi', '0005_rename_json_products_sale_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C')])),
                ('value', models.FloatField()),
                ('qty', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.AlterField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashApi.customer'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='products',
            field=models.TextField(default="{'type': 0, 'qty': 0, 'value': 0}"),
        ),
    ]
