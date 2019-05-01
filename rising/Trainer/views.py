from django.shortcuts import render
from django.http import HttpResponse

from Trainer.models import TrainerInfo
from Trainer.models import Document
from Trainer.forms import TrainerLogin
# Create your views here.

def Dashboard(request, docRecs):

    return render(request, "Trainer/Dashboard.html", context=docRecs)

def Profile(request):
    return render(request, "Trainer/Profile.html")

def TrainerFormView(request):
    form = TrainerLogin()

    if request.method == 'POST':
        form = TrainerLogin(request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            enteredpass = form.cleaned_data['password']
            records = TrainerInfo.objects.get(phone=phone)
            userRecs = {'records':records}
            if(str(userRecs['records'].password) == str(enteredpass)):
                usertopic = str(userRecs['records'].topic)
                docrec = Document.objects.filter(topic=usertopic)
                docRecs = {'docrec':docrec}
                # return Dashboard(request, docRecs)
                return render(request, "Trainer/Dashboard.html", context=docRecs)
        else:
            print("error")
    return render(request, 'Trainer/login.html', {'insertform': form})
