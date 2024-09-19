from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Visit, Appointment
from datetime import datetime
from .forms import PatientForm, VisitForm
from django.utils import timezone


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



def patient_details(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    form = PatientForm(instance=patient)
    
    upcoming_appointments = patient.appointments.filter(appointment_date__gte=timezone.now())
    visits = Visit.objects.filter(patient=patient).select_related('doctor', 'clinic')

    if request.method == 'POST':
        if 'save_patient' in request.POST:
            form = PatientForm(request.POST, instance=patient)
            if form.is_valid():
                form.save()
                return redirect('patient', pk=patient.pk)
        elif 'add_visit' in request.POST:
            visit_form = VisitForm(request.POST)
            if visit_form.is_valid():
                visit = visit_form.save(commit=False)
                visit.patient = patient 
                visit.save()
                return redirect('patient', pk=patient.pk)
    else:
        visit_form = VisitForm() 

    context = {
        'patient': patient,
        'form': form,
        'visit_form': visit_form,  
        'upcoming_appointments': upcoming_appointments,
        'visits': visits,
    }

    return render(request, 'patients/patient_detail.html', context)
