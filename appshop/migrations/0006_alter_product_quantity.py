# Generated by Django 4.0.2 on 2022-03-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appshop', '0005_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
