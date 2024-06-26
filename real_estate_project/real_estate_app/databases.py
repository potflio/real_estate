from django.shortcuts import render,redirect
from .models import *

def land_create(request):     
    land_resale = LandResale(
        email = request.POST['email'],
        length=request.POST['length'], 
        width = request.POST['width'],
        plot_area=request.POST['plot_area'],
        cent = request.POST['cent'],
        acre = request.POST['acre'],
        district = request.POST['district'],
        block = request.POST['block'],
        landmark = request.POST['landmark'],
        price_per_cent = request.POST['price_per_cent'],
        total_price = request.POST['total_price'],
        price_per_square_feet = request.POST['price_per_square_feet'],
        description = request.POST['description'],
        primary_number = request.POST['primary_number'],
        secondary_number = request.POST['secondary_number']
        )
    land_resale.save()
    return redirect('profile')

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

def email_login(request):
    login = LoginDetails(
        email = request.POST['email'],
        otp = request.POST['message']
    )
    login.save()
    return redirect('/')

def display_data(request):
    # Fetch data from MySQL database
    records = LandResale.objects.all()

    # Render the template with data
    return render(request, 'data_display.html', {'records': records}) 