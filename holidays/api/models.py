from django.db import models

# Create your models here.
class Holiday(models.Model):
    Holiday_Name=models.CharField(max_length=30)
    Date=models.CharField(max_length=20)
    Location=models.CharField(max_length=15)
    Shift=models.CharField(max_length=50)
    Details=models.CharField(max_length=50)
