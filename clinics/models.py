from django.db import models

class Clinic(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

    @property
    def num_doctors(self):
        return self.doctor_affiliations.count()

    @property
    def num_patients(self):
        from patients.models import Patient
        return Patient.objects.filter(appointments__clinic=self).distinct().count()