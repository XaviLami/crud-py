from django.db import models
import datetime
from django.utils import timezone

class Product(models.Model):
    name= models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.FileField(upload_to='product')
    createdAt = models.DateTimeField(auto_now_add=True)
def __str__(self):
        return str(self.name) + ": " + str(self.price) +" €"

