from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from .models import Question
from .forms import QuestionForm



def index(request):
  return render(request,'myfirstapp/index.html')

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "myfirstapp/create_view.html", context)

    #Detail View

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Question.objects.get(id = id)
         
    return render(request, "myfirstapp/detail_view.html", context)

#List View

def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = Question.objects.all()
		
	return render(request, "myfirstapp/list_view.html", context)

#Update view 

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/myfirstapp")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "myfirstapp/update_view.html", context)

#Delete view 

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Question, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/myfirstapp")
 
    return render(request, "myfirstapp/delete_view.html", context)

