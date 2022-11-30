from django.db import models
from django.contrib.auth.models import User

class Cakes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)


# Create your models here.
