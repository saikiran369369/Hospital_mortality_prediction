from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):

    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class mortality_prediction(models.Model):

    Fid= models.CharField(max_length=300)
    PatientId= models.CharField(max_length=300)
    ICU_AppointmentID= models.CharField(max_length=300)
    Gender= models.CharField(max_length=300)
    ScheduledDay= models.CharField(max_length=300)
    AppointmentDay= models.CharField(max_length=300)
    Age= models.CharField(max_length=300)
    Scheduled_Doctor= models.CharField(max_length=300)
    Scholarship= models.CharField(max_length=300)
    Hipertension= models.CharField(max_length=300)
    Diabetes= models.CharField(max_length=300)
    Alcoholism= models.CharField(max_length=300)
    Handcap= models.CharField(max_length=300)
    SMS_received= models.CharField(max_length=300)
    Patient_Diagnosis= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



