from django.urls import path
from .views import get_clinic_info, add_clinic

urlpatterns = [
    path('', add_clinic, name='add-clinic'),  
    path('<int:pk>/', get_clinic_info, name='clinic-info'),  
]
