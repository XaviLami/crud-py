from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Product
from .forms import ProductForm
# Home view
def home(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = Product.objects.all()
		
	return render(request, "appshop/home.html", context)
# Create view 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ProductForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appshop")
         
    context['form']= form
    return render(request, "appshop/create_view.html", context) 

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
         
    return render(request, "appshop/detail_view.html", context)

#Update view 

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/appshop")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "appshop/update_view.html", context)

#Delete view 

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/appshop")
 
    return render(request, "appshop/delete_view.html", context)
