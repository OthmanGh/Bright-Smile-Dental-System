from django import forms
from .models import Clinic
from doctors.models import DoctorAffiliation

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'city', 'state', 'phone_number', 'email']

class DoctorAffiliationForm(forms.ModelForm):
    class Meta:
        model = DoctorAffiliation
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