# Generated by Django 4.0.2 on 2022-03-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appshop', '0003_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
