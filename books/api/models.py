from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    image=models.ImageField(null=True,upload_to="bimages")
    discription=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BookDetail(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    liked_by = models.ManyToManyField(User,related_name="likes")

    def __str__(self):
        return self.book

    def like_count(self):
        return self.liked_by.all().count()

