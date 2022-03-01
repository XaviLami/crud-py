from django.contrib import admin
from django.db.models.fields import Field
from .models import Product

class ProductAdmin(admin.ModelAdmin):
        fields = ['name','price','picture']
admin.site.register(Product)
# Register your models here.
