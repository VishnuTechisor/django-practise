# from django.shortcuts import render
# from django.http import HttpResponse


# def showData(request):
#     return HttpResponse("<h1>show whole data</h1>")

# def create(request):
#     return HttpResponse('create data')

from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home(request):
    post=blogModel.objects.all()
    return render(request,"base.html",{"post":post})

def showData(request):
    post=formModel.objects.all()
    return render(request,"show.html",{"post":post})

def create(request):
    return HttpResponse("<h2>create user Data </h2>")

def showTable(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        description = request.POST.get("description")
        
        # Create a new instance of the formModel and save it
        form_instance = formModel(name=name, email=email, image=image, description=description)
        form_instance.save()
    
    post = formModel.objects.all()
    return render(request, "index.html", {"post": post})
