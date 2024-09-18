from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, DoctorClinicAffiliation
from .forms import DoctorForm
from patients.models import Patient

@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors.html', {'doctors': doctors})

