from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clinic
from .forms import ClinicForm
from doctors.models import DoctorClinicAffiliation
from doctors.forms import DoctorClinicAffiliationForm, AffiliationEditForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClinicSerializer
from patients.models import Patient
from django.contrib import messages


@login_required
def clinics_list(request):
    clinics = Clinic.objects.all()
    context = {
        'clinics': clinics
    }
    return render(request, 'clinics/clinics_list.html', context)



def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, id=pk)
    affiliations = DoctorClinicAffiliation.objects.filter(clinic=clinic)
    patients = Patient.objects.filter(appointments__clinic=clinic).distinct()

    if request.method == 'POST':
        if 'clinic_form' in request.POST:
            form = ClinicForm(request.POST, instance=clinic)

            if form.is_valid():
                form.save()
                messages.success(request, 'Clinic information updated successfully.')
                return redirect('clinic', pk=pk)
        
        elif 'affiliation_form' in request.POST:
            affiliation_form = DoctorClinicAffiliationForm(request.POST)

            if affiliation_form.is_valid():
                new_affiliation = affiliation_form.save(commit=False)
                new_affiliation.clinic = clinic
                new_affiliation.save()
                messages.success(request, 'Doctor affiliation added successfully.')
                return redirect('clinic', pk=pk)
        
        elif 'edit_affiliation' in request.POST:
            affiliation_id = request.POST.get('affiliation_id')
            affiliation = get_object_or_404(DoctorClinicAffiliation, id=affiliation_id)
            edit_form = AffiliationEditForm(request.POST, instance=affiliation)

            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, 'Doctor affiliation updated successfully.')
                return redirect('clinic', pk=pk)
    else:
        form = ClinicForm(instance=clinic)
        affiliation_form = DoctorClinicAffiliationForm()

    affiliations_with_forms = [(affiliation, AffiliationEditForm(instance=affiliation)) for affiliation in affiliations]

    context = {
        'clinic': clinic,
        'form': form,
        'affiliation_form': affiliation_form,
        'affiliations_with_forms': affiliations_with_forms,
        'patients': patients,
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