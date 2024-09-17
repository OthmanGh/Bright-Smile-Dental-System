from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Clinic

@login_required
def clinics_list(request):
    clinics = Clinic.objects.all()
    context = {
        'clinics': clinics
    }
    return render(request, 'clinics/clinics_list.html', context)

