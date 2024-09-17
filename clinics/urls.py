from django.urls import path
from .views import clinics_list, clinic_detail

urlpatterns = [
    path('', clinics_list, name='clinics'),
    path('clinic/<int:pk>', clinic_detail, name='clinic'),
]
