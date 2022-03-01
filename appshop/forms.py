from django import forms
from .models import Product
 
 
# creating a form
class ProductForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Product
        fields="__all__"
 
        # specify fields to be used
       