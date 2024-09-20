from django.urls import path
from .views import clinics_list, clinic_detail, get_clinic_info

urlpatterns = [
    path('', clinics_list, name='clinics'),
    path('<int:pk>/', clinic_detail, name='clinic'),
    path('clinics/<int:pk>/', get_clinic_info, name='clinic_info')
]
