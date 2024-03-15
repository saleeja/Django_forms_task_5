from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
from .forms import MedicalRecordForm
from .forms import MedicalRecordForms
from .models import MedicalRecord


# 4.Create a view for adding details to second model (Use model forms)
def add_patient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')  
    return render(request, 'add_patient.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


"""NormalForm"""
def add_medical_record(request):
    form = MedicalRecordForm()
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data['patient']
            diagnosis = form.cleaned_data['diagnosis']
            MedicalRecord.objects.create(patient=patient, diagnosis=diagnosis)
            return redirect('medical_record_list') 
    return render(request, 'add_record.html', {'form': form})


def medical_record_list(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'medical_record.html', {'medical_records': medical_records})


def upload_record(request):
    if request.method == 'POST':
        form = MedicalRecordForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploaded_files')
    else:
        form = MedicalRecordForms()
    return render(request, 'upload_record.html', {'form': form})



def uploaded_files(request):
    records = MedicalRecord.objects.all()
    return render(request, 'uploaded_files.html', {'records': records})
