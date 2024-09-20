from django.urls import path
from .views import add_doctor, doctor_detail

urlpatterns = [
    path('', add_doctor, name='add-doctor'), 
    path('<int:pk>/', doctor_detail, name='doctor-info'),
]
