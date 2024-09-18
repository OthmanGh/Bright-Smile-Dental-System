from django.shortcuts import render
from .models import Patient

def patients_list(request):
    patients = Patient.objects.all()

    context = {
        'patients': patients
    }

    return render(request, 'patients/patients.html',  context)