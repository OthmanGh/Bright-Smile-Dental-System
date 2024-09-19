from django import forms
from .models import Clinic

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'phone_number', 'email']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'phone_number': forms.TextInput(attrs={'maxlength': 15}),
            'email': forms.EmailInput(attrs={'maxlength': 254}),
        }