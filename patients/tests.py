from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Patient

class PatientTests(TestCase):
    def test_add_patient(self):
        url = reverse('add-patient')
        data = {
            "name": "Steve Havrd",
            "date_of_birth": "2000-09-30",
            "address": "123 street St",
            "phone_number": "452-655-7426",
            "last_4_ssn": "5724",
            "gender": "Male"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1) 
        self.assertEqual(Patient.objects.last().name, 'Steve Havrd')

    def test_add_patient_invalid_data(self):
        url = reverse('add-patient')
        data = {
            "name": "Steve Havrd",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
