from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clinic
from .forms import ClinicForm

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
    doctor_affiliations = clinic.doctor_affiliations.all()

    if request.method == 'POST':
        form = ClinicForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('clinic_detail', pk=clinic.pk)
    else:
        form = ClinicForm(instance=clinic)

    context = {
        'clinic': clinic,
        'form': form,
        'doctor_affiliations': doctor_affiliations
    }
    return render(request, 'clinics/clinic_detail.html', context)

