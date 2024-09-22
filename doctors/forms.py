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
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        empty_label="Select Doctor",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = DoctorClinicAffiliation
        fields = ['doctor', 'office_address', 'working_days', 'start_time', 'end_time']
        widgets = {
            'office_address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'working_days': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'class': 'form-control'}),
        }


class AffiliationEditForm(forms.ModelForm):
    class Meta:
        model = DoctorClinicAffiliation
        fields = ['office_address', 'working_days', 'start_time', 'end_time']
        widgets = {
            'office_address': forms.Textarea(attrs={'rows': 3}),
            'working_days': forms.CheckboxSelectMultiple(),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }