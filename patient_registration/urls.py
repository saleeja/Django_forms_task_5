from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('list/', views.patient_list, name='patient_list'),
    path('add-medical-record/', views.add_medical_record, name='add_medical_record'),
    path('medical-records/', views.medical_record_list, name='medical_record_list'),
    path('upload-record/', views.upload_record, name='upload_record'),
    path('uploaded-files/', views.uploaded_files, name='uploaded_files'),
]
