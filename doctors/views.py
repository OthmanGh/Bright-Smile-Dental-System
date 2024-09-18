from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, DoctorClinicAffiliation
from .forms import DoctorForm
from patients.models import Patient

@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors.html', {'doctors': doctors})


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
    
    return render(request, 'doctors/doctor.html', context)