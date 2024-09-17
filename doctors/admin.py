from django.contrib import admin
from .models import Doctor, DoctorClinicAffiliation

admin.site.register(Doctor)
admin.site.register(DoctorClinicAffiliation)