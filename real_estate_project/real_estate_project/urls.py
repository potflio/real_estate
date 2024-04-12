from django.contrib import admin
from django.urls import path
from real_estate_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base',views.base,name='base'),
    path('index',views.index, name = 'index'),
    path('land_create/',views.land_create, name='land_create'),
    path('residential_rent_create/',views.residential_rent_create ,name = 'residential_rent_create'),
    path('post_property',views.post_property, name='post_property'),
    path('residential_rent_form',views.residential_rent_form ,name='residential_rent_form'),
    path('residential_resale_form',views.residential_resale_form ,name='residential_resale_form'),
    path('residential_pg_hostel_form',views.residential_pg_hostel_form ,name='residential_pg_hostel_form'),
    path('residential_flatmates_form',views.residential_flatmates_form ,name='residential_flatmates_form'),
    path('commercial_rent_form',views.commercial_rent_form ,name='commercial_rent_form'),
    path('commercial_sale_form',views.commercial_sale_form ,name='commercial_sale_form'),
    path('land_resale_form',views.land_resale_form,name='land_resale_form'),
    
]
