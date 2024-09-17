from django.db import models
from doctors.models import Doctor  

PROCEDURES = [
    ('cleaning', 'Cleaning'),
    ('filling', 'Filling'),
    ('root_canal', 'Root Canal'),
    ('crown', 'Crown'),
    ('whitening', 'Teeth Whitening'),
]

class Patient(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    last_4_ssn = models.CharField(max_length=4)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return self.name


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE) 
    visit_date = models.DateTimeField()
    procedures_done = models.CharField(max_length=50, choices=PROCEDURES)
    doctor_notes = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.visit_date} - {self.procedures_done}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE) 
    procedure = models.CharField(max_length=50, choices=PROCEDURES)
    appointment_date = models.DateTimeField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.appointment_date} for {self.procedure}"
