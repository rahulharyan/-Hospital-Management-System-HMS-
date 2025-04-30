from django.db import models

# Create your models here.

class AddPatient(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    phone=models.IntegerField()
