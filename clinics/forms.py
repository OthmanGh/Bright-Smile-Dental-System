from django import forms
from .models import Clinic
from doctors.models import DoctorAffiliation

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'city', 'state', 'phone_number', 'email']

