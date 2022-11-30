from django.db import models

# Create your models here

class Employe(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    DOB=models.CharField(max_length=15)
    Department=models.CharField(max_length=50)
    Post=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Contact_Number=models.PositiveIntegerField()
    Adrees_Field_1=models.CharField(max_length=100)
    Adrees_Field_1=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Pincode=models.PositiveIntegerField()
