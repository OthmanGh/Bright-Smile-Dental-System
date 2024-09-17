from django import forms
from .models import Clinic

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'city', 'state', 'phone_number', 'email']

