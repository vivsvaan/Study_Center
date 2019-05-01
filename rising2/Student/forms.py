from django import forms
from django.contrib.auth.models import User
from Student.models import StudentProfileInfo

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("username", "email", "password")

class StudentProfileInfoForm(forms.ModelForm):

    class Meta():
        model = StudentProfileInfo
        fields = ("phone",)
