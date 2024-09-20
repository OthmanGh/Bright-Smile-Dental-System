from django.db import models
from multiselectfield import MultiSelectField
from datetime import time

class Doctor(models.Model):
    SPECIALTY_CHOICES = (
        ('cleaning', 'Cleaning'),
        ('filling', 'Filling'),
        ('root_canal', 'Root Canal'),
        ('crown', 'Crown'),
        ('teeth_whitening', 'Teeth Whitening'),
    )

    npi = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    specialties = MultiSelectField(choices=SPECIALTY_CHOICES, default=[])
    clinics = models.ManyToManyField('clinics.Clinic', through='DoctorClinicAffiliation', related_name='doctors')

    def __str__(self):
        return self.name

    @property
    def num_clinics(self):
        return self.clinics.count()

    @property
    def num_patients(self):
        from patients.models import Patient
        return Patient.objects.filter(appointments__doctor=self).distinct().count()


class DoctorClinicAffiliation(models.Model):
    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='affiliations')
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE, related_name='doctor_affiliations')
    office_address = models.TextField()
    working_days = MultiSelectField(choices=DAY_CHOICES, blank=True)
    start_time = models.TimeField(default=time(9, 0))
    end_time = models.TimeField(default=time(17, 0))

    class Meta:
        unique_together = ('doctor', 'clinic')

    def __str__(self):
        return f"{self.doctor.name} at {self.clinic.name}"
