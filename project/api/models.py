from django.db import models

# Create your models here.

class Project(models.Model):
    Project_id=models.PositiveIntegerField()
    Project_Title=models.CharField(max_length=30)
    Department=models.CharField(max_length=15)
    Project_priority=models.CharField(max_length=50)
    Client=models.CharField(max_length=50)
    Price=models.PositiveIntegerField()
    Project_start_Date=models.CharField(max_length=30)
    Project_End_Date = models.CharField(max_length=30)
    Team=models.CharField(max_length=50)
    options=(
        ("Active","Active"),
        ("Completed","completed"),
        ("Running", "Running"),
        ("pending", "pending"),
        ("Not started", "Not started"),
        ("Cancelled", "cancelled"),
    )
    Work_status=models.CharField(max_length=30,choices=options)
    Description=models.CharField(max_length=100)
