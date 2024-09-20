from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Clinic
from rest_framework import status

class APITests(APITestCase):
    
    def setUp(self):
        self.clinic_url = reverse('add-clinic')
    
        self.valid_clinic_data = {
                "name": "Health Clinic",
                "email": "support@pearlwhite.com",
                "phone_number": "+1-555-123-4567",
                "address": "456 Health St",
                "city": "Chicago",
                "state": "IL",
            }

    def test_add_valid_clinic(self):
        response = self.client.post(self.clinic_url, data=self.valid_clinic_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Clinic.objects.count(), 1)
        self.assertEqual(Clinic.objects.get().name, "Health Clinic")


    def test_add_invalid_clinic(self):
        invalid_data = self.valid_clinic_data.copy()
        invalid_data["name"] = "" 
        response = self.client.post(self.clinic_url, data=invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Clinic.objects.count(), 0)


    def test_get_clinic_info(self):
        clinic = Clinic.objects.create(name="Health Clinic", address="456 Health St", phone_number="+1-555-123-4567")
        response = self.client.get(reverse('clinic-info', args=[clinic.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Health Clinic")


    def test_get_invalid_clinic_info(self):
        response = self.client.get(reverse('clinic-info', args=[999])) 
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)