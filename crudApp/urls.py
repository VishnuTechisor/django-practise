from django.contrib import admin
from django.urls import path
from crudApp import views


urlpatterns = [
    path("", views.home),
    path("show/", views.showData),
    path("create/", views.create),
    path("showtable/",views.showTable)
    ]
