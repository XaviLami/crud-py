# Generated by Django 4.0.2 on 2022-02-28 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appshop', '0002_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='product/'),
        ),
    ]