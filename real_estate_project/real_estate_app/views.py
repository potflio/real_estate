from django.shortcuts import render,redirect
from .models import LandResale


def base(request):
    return render(request,'base.html')

def welcome(request):
    return render(request,"welcome.html")
    
def index(request):
    members = LandResale.objects.all()[:3]
    context = {'member' : members}
    return render(request,'index.html',context)


def post_property(request):
    return render(request,'post_property.html')

def residential_rent_form(request):
    return render(request,"residential_rent_form.html")

def residential_resale_form(request):
    return render(request,"residential_resale_form.html")

def residential_pg_hostel_form(request):
    return render(request,"residential_pg_hostel_form.html")

def residential_flatmates_form(request):
    return render(request,"residential_flatmates_form.html")

def commercial_rent_form(request):
    return render(request,"commercial_rent_form.html")

def commercial_sale_form(request):
    return render(request,"commercial_sale_form.html")

def land_resale_form(request):
    return render(request,'land_resale_form.html')

def profile(request):
    return render(request,"profile.html")

def example(request):
    return render(request,"example.html")

def land_properties_view(request):
    return render(request,"land_properties_view.html")

def property_view(request):
    return render(request,"property_view.html")

def data_processing(request):
    return render(request,"data_processing.html")


def land_view(request, id):
    members = LandResale.objects.get(id=id)
    context = {'member': members}
    return render(request, 'land_view.html', context)

def plans(request):
    return render(request,"plans.html")