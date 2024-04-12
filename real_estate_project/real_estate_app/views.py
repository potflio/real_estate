from django.shortcuts import render,redirect
from .models import *


def base(request):
    return render(request,'base.html')

def index(request):
    return render(request,'index.html')

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

def land_create(request):
    land_resale = LandResale(
        plot_area=request.POST['plot_area'],
        length=request.POST['length'], 
        width = request.POST['width'],
        city = request.POST['city'],
        locality = request.POST['locality'],
        landmark = request.POST['landmark'],
        expected_price = request.POST['expected_price'],
        description = request.POST['description']
        )
    land_resale.save()
    return redirect('/')

def residential_rent_create(request):
    residential_rent = ResidentialRent(
        bhk=request.POST['bhk'],
        floor=request.POST['floor'],
        totalfloor = request.POST['totalfloor'],
        property_age = request.POST['property_age'],
        builtup_area = request.POST['builtup_area'],
        city = request.POST['city'],
        locality = request.POST['locality'],
        landmark = request.POST['landmark'],
        rent = request.POST['rent'],
        lease = request.POST['lease'],
        expected_rent = request.POST['expected_rent'],
        expected_deposit = request.POST['expected_deposit'],
        expected_lease_amount = request.POST['expected_lease_amount'],
        maintenance = request.POST['maintenance'],
        description = request.POST['description']
    )
    residential_rent.save()
    return redirect('/')