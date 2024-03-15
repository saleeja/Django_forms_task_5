from django import forms
from .models import Patient
from .models import MedicalRecord

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__' 

# NormalForms
class MedicalRecordForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    diagnosis = forms.CharField(max_length=200)
    
class MedicalRecordForms(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'report_file']


