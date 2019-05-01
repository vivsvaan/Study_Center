from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=20)

class PracticeQues(models.Model):
    question = models.CharField(max_length=400)
    studentAns = models.CharField(max_length=264, default="")
    rightAns = models.CharField(max_length=264)
