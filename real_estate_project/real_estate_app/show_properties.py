from django.shortcuts import render,redirect
from .models import *

def land_properties_show(request):
    land_properties = LandResale.objects.all()
    return render(request,'land_properties_show.html',{'land_properties':land_properties})

def land_properties_show_index(request):
    land_properties = LandResale.objects.all()[:3]
    return render(request,'index.html',{'land_properties':land_properties})

def property_view(request):
    property_view = LandResale.objects.all()
    return render(request,'property_view.html',{'property_view':property_view})