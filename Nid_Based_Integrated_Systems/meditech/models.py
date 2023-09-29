from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.
class Students(models.Model):
    sId = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
class Meta:
    db_table = "students"
class newMedication(models.Model):
    PatientNID = models.IntegerField()
    PatientName = models.CharField(max_length=255)
    PatientAge = models.IntegerField()
    StartDate = models.DateField()
    EndDate= models.DateField()
    DiseaseType = models.CharField(max_length=100)
    Medication = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name