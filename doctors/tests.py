from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Doctor

class DoctorTests(TestCase):
    def setUp(self):
        Doctor.objects.create(
            npi="9876543210",
            name="Dr. Existing Doctor",
            email="existing.doctor@example.com",
            phone_number="+1-555-555-5555",
            specialties=["cleaning"]
        )

    def test_add_doctor(self):
        url = reverse('add-doctor')
        data = {
            "npi": "1234569999",
            "name": "Dr. Jane Jane",
            "email": "janejane@example.com",
            "phone_number": "0987654321",  
            "specialties": ["cleaning", "filling"]
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doctor.objects.count(), 2) 
        self.assertEqual(Doctor.objects.last().name, 'Dr. Jane Jane')

    def test_add_doctor_invalid_data(self):
        url = reverse('add-doctor')
        data = {
            "name": "Dr. Jane Jane",
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
