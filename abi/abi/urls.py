from django.shortcuts import render
from django.contrib import admin 
from django.urls import path 
from myapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('bmicalculation/',views.bmi,name="bmicalculation"),
    path('',views.bmi,name="bmicalculationroot")
]