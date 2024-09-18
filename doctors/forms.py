from django import forms
from .models import Doctor, DoctorClinicAffiliation

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'phone_number', 'specialties']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialties': forms.CheckboxSelectMultiple,  
        }



class DoctorClinicAffiliationForm(forms.ModelForm):
    class Meta:
        model = DoctorClinicAffiliation
        fields = ['doctor', 'office_address', 'working_days', 'working_hours']
        widgets = {
            'working_days': forms.CheckboxSelectMultiple(choices=[
                ('Monday', 'Monday'),
                ('Tuesday', 'Tuesday'),
                ('Wednesday', 'Wednesday'),
                ('Thursday', 'Thursday'),
                ('Friday', 'Friday'),
                ('Saturday', 'Saturday'),
                ('Sunday', 'Sunday'),
            ]),
            'working_hours': forms.TextInput(attrs={'placeholder': '{"start": "09:00", "end": "17:00"}'}),
        }

