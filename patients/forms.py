from django import forms    
from .models import Patient, Appointment, Visit


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'date_of_birth', 'address', 'phone_number', 'last_4_ssn', 'gender']


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['doctor', 'clinic', 'visit_date', 'procedures_done', 'doctor_notes']
        widgets = {
            'visit_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'clinic', 'procedure', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


