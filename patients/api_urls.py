from django.urls import path
from .views import add_patient, patient_details

urlpatterns = [
    path('', add_patient, name='add-patient'), 
    path('<int:pk>/', patient_details, name='patient-info'), 
]
