from django import forms
from .models import Doctor, DoctorClinicAffiliation

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['npi','name', 'email', 'phone_number', 'specialties']  
        widgets = {
            'npi': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialties': forms.CheckboxSelectMultiple,  
        }
        


class DoctorClinicAffiliationForm(forms.ModelForm):
    class Meta:
        model = DoctorClinicAffiliation
        fields = ['doctor', 'office_address', 'working_days', 'working_hours']
