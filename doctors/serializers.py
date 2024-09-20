from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    specialties = serializers.ListField(
        child=serializers.ChoiceField(choices=[choice[0] for choice in Doctor.SPECIALTY_CHOICES]),
        allow_empty=True
    )

    class Meta:
        model = Doctor
        fields = '__all__'
