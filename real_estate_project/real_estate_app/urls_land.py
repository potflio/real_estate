from django.urls import path
from . import databases,views,show_property_details,show_properties

urlpatterns = [
    path('land_create/',databases.land_create, name='land_create'),
    path('land_resale_form',views.land_resale_form,name='land_resale_form'),
    path('land_properties_show',show_properties.land_properties_show,name='land_properties_show'),
    path('land_view/<id>',views.land_view, name='land_view'),
]