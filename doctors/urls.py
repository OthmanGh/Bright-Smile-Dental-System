from django.urls import path
from .views import doctors_list, doctor_detail, add_doctor

urlpatterns = [
    path('', doctors_list, name='doctors'),
    path('doctor/<int:pk>/', doctor_detail, name='doctor'),
    path('doctors/', add_doctor, name='add_doctor'),
]
