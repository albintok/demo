from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Restuarents(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    rating=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dishes(models.Model):
    restuarent=models.ForeignKey(Restuarents,on_delete=models.CASCADE)
    dish=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)
    image=models.ImageField(null=True,upload_to="pics")
    price=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.dish


class Buys(models.Model):
    name=models.ForeignKey(Dishes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-buy","in-buy"),
        ("buyed","buyed")
    )
    status=models.CharField(max_length=10,choices=options,default="in-buy")
    
    def __str__(self):
        return self.name

