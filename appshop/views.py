from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Home view
def home(request):
  return render(request,'appshop/home.html')
# Create view 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "appshop/create_view.html", context) 

