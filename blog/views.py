from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.shortcuts import render
from .forms import BlogForm
from .models import BlogModel

def create_blog(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request, "create_blog.html", context)

def list_blog(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["dataset"] = BlogModel.objects.all()
          
    return render(request, "list_blog.html", context)
    
def detail_blog(request, pk):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = BlogModel.objects.get(id = pk)
          
    return render(request, "detail_blog.html", context)

def update_blog(request, pk):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    obj = get_object_or_404(BlogModel, id = pk)
  
    # pass the object as instance in form
    form = BlogForm(request.POST or None, instance = obj)
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+pk)
  
    # add form dictionary to context
    context["form"] = form
  
    return render(request, "update_blog.html", context)

def delete_blog(request, pk):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    obj = get_object_or_404(BlogModel, id = pk)
  
  
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
  
    return render(request, "delete_blog.html", context)