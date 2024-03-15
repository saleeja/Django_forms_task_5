from django.contrib import admin
from .models import Patient,MedicalRecord

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','gender','email','phone_number','address')

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'report_file')

admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(Patient, PatientAdmin)