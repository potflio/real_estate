from django.shortcuts import render, redirect
from real_estate_app.models import LandResale

def land_view(request, id):
    members = LandResale.objects.get(id=id)
    context = {'member': members}
    return render(request, "land_view.html", context)


