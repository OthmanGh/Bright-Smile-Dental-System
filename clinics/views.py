from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clinic
from .forms import ClinicForm
from doctors.models import DoctorClinicAffiliation, Doctor
from doctors.forms import DoctorClinicAffiliationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClinicSerializer

@login_required
def clinics_list(request):
    clinics = Clinic.objects.all()
    context = {
        'clinics': clinics
    }
    return render(request, 'clinics/clinics_list.html', context)


@login_required
def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)

    form = ClinicForm(instance=clinic)
    affiliation_form = DoctorClinicAffiliationForm()

    if request.method == 'POST':
        if 'clinic_form' in request.POST:
            form = ClinicForm(request.POST, instance=clinic)
            if form.is_valid():
                form.save()
                return redirect('clinic', pk=clinic.pk)

        elif 'affiliation_form' in request.POST:
            affiliation_id = request.POST.get('affiliation_id')

            if affiliation_id:
                affiliation = get_object_or_404(DoctorClinicAffiliation, pk=affiliation_id)
                form = DoctorClinicAffiliationForm(request.POST, instance=affiliation)
            else:
                form = DoctorClinicAffiliationForm(request.POST)
                form.instance.clinic = clinic

            if form.is_valid():
                form.save()
                return redirect('clinic', pk=clinic.pk)
            
            else:
                print(form.errors) 

    affiliations = DoctorClinicAffiliation.objects.filter(clinic=clinic)

    doctors = Doctor.objects.filter(affiliations__clinic=clinic).distinct()

    affiliations_with_hours = []

    for affiliation in affiliations:
        working_hours = []
        for day in affiliation.working_days:
            hours = affiliation.working_hours.get(day, "")
            working_hours.append(f"{day}: {hours}")

        affiliations_with_hours.append({
            'doctor': affiliation.doctor,
            'office_address': affiliation.office_address,
            'working_hours': ", ".join(working_hours),
            'id': affiliation.pk
        })

    context = {
        'clinic': clinic,
        'form': form,
        'affiliation_form': affiliation_form,
        'affiliations_with_hours': affiliations_with_hours,
        'doctors': doctors,  
    }
    return render(request, 'clinics/clinic_detail.html', context)



@api_view(['GET'])
def get_clinic_info(request, pk):
    try:
        clinic = Clinic.objects.get(pk=pk)
        
    except Clinic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClinicSerializer(clinic)
    return Response(serializer.data)


@api_view(['POST'])
def add_clinic(request):
    if request.method == 'POST':
        serializer = ClinicSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)