from django.contrib import admin
from django.conf.urls.static import settings
from django.urls import path,include
from real_estate_app import views,databases,show_properties,show_property_details
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name='welcome'),
    path('base',views.base,name='base'),
    path('index',views.index, name = 'index'),
    path('profile/',views.profile, name = 'profile'),
    path('residential_rent_create/',databases.residential_rent_create ,name = 'residential_rent_create'),
    path('post_property',views.post_property, name='post_property'),
    path('residential_rent_form',views.residential_rent_form ,name='residential_rent_form'),
    path('residential_resale_form',views.residential_resale_form ,name='residential_resale_form'),
    path('residential_pg_hostel_form',views.residential_pg_hostel_form ,name='residential_pg_hostel_form'),
    path('residential_flatmates_form',views.residential_flatmates_form ,name='residential_flatmates_form'),
    path('commercial_rent_form',views.commercial_rent_form ,name='commercial_rent_form'),
    path('commercial_sale_form',views.commercial_sale_form ,name='commercial_sale_form'),
    path('property_view',show_properties.property_view,name='property_view'),
    path('email/', include('real_estate_app.urls')),
    path('land/',include('real_estate_app.urls_land')),
    path('plans/',views.plans,name="plans"),
    path('data_processing',views.data_processing,name='data_processing'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
