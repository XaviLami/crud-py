from django.contrib import admin
from django.db.models.fields import Field
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
        fields = ['date','text']
admin.site.register(Question)
# Register your models here.
