from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Clinic

class ClinicTests(TestCase):
    def setUp(self):
        self.clinic = Clinic.objects.create(
            name="Garden State Dental Care",
            address="789 Oak Blvd, Suite 5",
            city="Newark",
            state="NJ",
            phone_number="973-555-7890",
            email="info@gardensatedental.com",
        )

    def test_get_clinic_info(self):
        url = reverse('clinic-info', kwargs={'pk': self.clinic.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.clinic.name)


    def test_get_clinic_info_not_found(self):
        url = reverse('clinic-info', kwargs={'pk': 999}) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_add_clinic(self):
        url = reverse('add-clinic')
        data = {
            "name": "New Clinic",
            "address": "123 Elm St",
            "city": "New City",
            "state": "NC", 
            "phone_number": "9876543210",
            "email": "newclinic@example.com",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Clinic.objects.count(), 2)  
        self.assertEqual(Clinic.objects.last().name, 'New Clinic')


    def test_add_clinic_invalid_data(self):
        url = reverse('add-clinic')
        data = {
            "name": "New Clinic",
            "address": "123 Elm St",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
