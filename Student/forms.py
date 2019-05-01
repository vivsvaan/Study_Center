from django import forms
from Student.models import StudentInfo, PracticeQues
from django.core import validators

class StudentLogin(forms.ModelForm):
    phone = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = StudentInfo
        fields = ( "phone", "password")

class PracticeQuesForm(forms.ModelForm):
    # studentAns = forms.CharField()
    # rightAns = forms.CharField()
    # question = forms.CharField(max_length=400)

    class Meta:
        model = PracticeQues
        fields = ( "studentAns","question")
