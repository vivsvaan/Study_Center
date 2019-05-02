from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    datestamp = models.DateField(auto_now_add=True)
    liked = models.CharField(max_length=50, default="")
