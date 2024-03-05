# from django.shortcuts import render
# from django.http import HttpResponse


# def showData(request):
#     return HttpResponse("<h1>show whole data</h1>")

# def create(request):
#     return HttpResponse('create data')

from django.http import HttpResponse
from django.shortcuts import render
from .models import blogModel


def home(request):
    post=blogModel.objects.all()
    return render(request,"base.html",{"post":post})

def showData(request):
    return HttpResponse("<h1>welcome to my channel </h1>")

def create(request):
    return HttpResponse("<h2>create user Data </h2>")
def showTable(request):
    return render(request,"index.html",{"name":"vishnu..........!!!"})
