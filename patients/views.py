from django.shortcuts import render
from .models import Patient, Visit, Appointment
from datetime import datetime

from django.shortcuts import render
from .models import Patient, Visit, Appointment
from datetime import datetime

def patients_list(request):
    patients = Patient.objects.all()

    for patient in patients:
        last_visit = Visit.objects.filter(patient=patient).order_by('-visit_date').first()

        next_appointment = Appointment.objects.filter(patient=patient, appointment_date__gte=datetime.now()).order_by('appointment_date').first()

        patient.last_visit = last_visit
        patient.next_appointment = next_appointment

    context = {
        'patients': patients
    }

    return render(request, 'patients/patients.html', context)

