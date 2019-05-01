from django.db import models

# Create your models here.

class TrainerInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    topic = models.CharField(max_length=50, default="")

class Document(models.Model):
    datestamp = models.DateField(auto_now_add=True)
    document = models.FileField(upload_to='documents/')
    title = models.CharField(max_length=50)
    topic = models.CharField(max_length=50, default="")
