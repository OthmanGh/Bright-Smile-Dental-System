from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),  
    path('clinics/', include('clinics.urls')),
    path('doctors/', include('doctors.urls')), 
    path('patients/', include('patients.urls')), 

    # API routes
    path('api/clinics/', include('clinics.api_urls')),  
    path('api/doctors/', include('doctors.api_urls')),  
    path('api/patients/', include('patients.api_urls')),  
]
