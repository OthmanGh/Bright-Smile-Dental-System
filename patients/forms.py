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

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'clinic', 'procedure', 'appointment_date']