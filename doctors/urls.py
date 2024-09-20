from django.urls import path
from .views import doctors_list, doctor_detail

urlpatterns = [
    path('', doctors_list, name='doctors'),
    path('doctor/<int:pk>/', doctor_detail, name='doctor'),
]
