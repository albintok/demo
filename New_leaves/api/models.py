from django.db import models

# Create your models here.
class Leaves(models.Model):
    Name=models.CharField(max_length=30)
    Leave_Type=models.CharField(max_length=30)
    Leave_from=models.CharField(max_length=15)
    Leave_To=models.CharField(max_length=50)
    No_of_Days=models.PositiveIntegerField()
    Status=models.CharField(max_length=50)
    Reason=models.CharField(max_length=100)
