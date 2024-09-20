from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, DoctorClinicAffiliation
from .forms import DoctorForm
from patients.models import Patient
from .serializers import DoctorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors_list.html', {'doctors': doctors})


@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    
    affiliations = DoctorClinicAffiliation.objects.filter(doctor=doctor)
    patients = Patient.objects.filter(appointments__doctor=doctor).distinct()

    context = {
        'doctor': doctor,
        'form': form,
        'affiliations': affiliations,
        'patients': patients,
    }
    
    return render(request, 'doctors/doctor_detail.html', context)


@api_view(['POST'])
def add_doctor(request):
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)