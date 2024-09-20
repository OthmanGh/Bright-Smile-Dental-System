from django.urls import path
from .views import patients_list, patient_details

urlpatterns = [
    path('', patients_list, name='patients'),
    path('patient/<int:pk>/', patient_details, name='patient'),
]
