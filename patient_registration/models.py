from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=200)
    report_file = models.FileField(upload_to='medical_records/')