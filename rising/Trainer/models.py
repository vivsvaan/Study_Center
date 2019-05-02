from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=12)
    topic = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.user.username

class Document(models.Model):
    datestamp = models.DateField(auto_now_add=True)
    document = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=50, default="")
