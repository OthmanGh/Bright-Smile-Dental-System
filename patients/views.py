from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Visit, Appointment
from datetime import datetime
from .forms import PatientForm, VisitForm, AppointmentForm
from django.utils import timezone
from rest_framework.decorators import api_view
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework import status

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
    
    upcoming_appointments = patient.appointments.filter(appointment_date__gte=timezone.now()).order_by('appointment_date')

    next_appointment = upcoming_appointments.first() if upcoming_appointments.exists() else None
    
    visits = Visit.objects.filter(patient=patient).select_related('doctor', 'clinic')

    appointment_form = AppointmentForm()

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

        elif 'add_appointment' in request.POST:
            appointment_form = AppointmentForm(request.POST)

            if appointment_form.is_valid():
                appointment = appointment_form.save(commit=False)
                appointment.patient = patient
                appointment.save()
                return redirect('patient', pk=patient.pk)

    else:
        visit_form = VisitForm() 

    context = {
        'patient': patient,
        'form': form,
        'visit_form': visit_form,  
        'upcoming_appointments': upcoming_appointments,
        'appointment_form': appointment_form,  
        'visits': visits,
        'next_appointment': next_appointment
    }

    return render(request, 'patients/patient_detail.html', context)



@api_view(['POST'])
def add_patient(request):
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
