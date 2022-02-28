
from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    text= models.CharField(max_length=200)
    date = models.DateTimeField('date')
def __str__(self):
        return self.text
# Create your models here.
