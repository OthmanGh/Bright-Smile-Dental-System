from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('clinics/', include('clinics.urls')),
    path('doctors/', include('doctors.urls')),
    path('patients/', include('patients.urls')),
    path('api/', include('clinics.urls')),
    path('api/', include('doctors.urls')),
    path('api/', include('patients.urls')),

]
