from django.urls import path
from .views import add_doctor

urlpatterns = [
    path('', add_doctor, name='add-doctor'), 
]
