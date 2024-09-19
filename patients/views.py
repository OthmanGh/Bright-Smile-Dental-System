from django.shortcuts import render, redirect
from .models import Patient, Visit, Appointment
from datetime import datetime

def patients_list(request):
    patients = Patient.objects.all()

    for patient in patients:
        last_visit = Visit.objects.filter(patient=patient).order_by('-visit_date').first()

        if last_visit:
            patient.last_visit_date = last_visit.visit_date
            patient.last_visit_doctor = last_visit.doctor
            patient.last_visit_procedure = last_visit.procedures_done
        else:
            patient.last_visit_date = None
            patient.last_visit_doctor = None
            patient.last_visit_procedure = None
        
        next_appointment = Appointment.objects.filter(patient=patient, appointment_date__gte=datetime.now()).order_by('appointment_date').first()
        if next_appointment:
            patient.next_appointment_date = next_appointment.appointment_date
            patient.next_appointment_doctor = next_appointment.doctor
            patient.next_appointment_procedure = next_appointment.procedure
        else:
            patient.next_appointment_date = None
            patient.next_appointment_doctor = None
            patient.next_appointment_procedure = None

    context = {
        'patients': patients
    }

    return render(request, 'patients/patients_list.html', context)


