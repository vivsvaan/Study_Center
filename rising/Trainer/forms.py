from django import forms
from Trainer.models import TrainerInfo
from Trainer.models import Document
from django.core import validators

class TrainerLogin(forms.ModelForm):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    # email = forms.EmailField()
    # vemail = forms.EmailField(label='Enter email again')
    phone = forms.CharField()
    password = forms.CharField()

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vemail = all_clean_data['vemail']
    #     if email != vemail:
    #         raise forms.ValidationError('Email should be same')

    class Meta:
        model = TrainerInfo
        fields = ( "phone", "password")


# class UploadDocs(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('title', 'document', )
