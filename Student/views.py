from django.shortcuts import render
from django.http import HttpResponse

from Student.models import StudentInfo, PracticeQues
from Student.forms import StudentLogin, PracticeQuesForm
# Create your views here.

def Dashboard(request):
    return HttpResponse("logged in")


def StudentFormView(request):
    form = StudentLogin()

    if request.method == 'POST':
        form = StudentLogin(request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            enteredpass = form.cleaned_data['password']
            records = StudentInfo.objects.get(phone=phone)
            userRecs = {'records':records}
            if(str(userRecs['records'].password) == str(enteredpass)):
                return Dashboard(request)
        else:
            print("error")
    return render(request, 'Student/login.html', {'insertform': form})


def PracticeQuesAns(request):
    responses = PracticeQues.objects.all()
    responseRecs = {'responses':responses}
    return render(request, 'Student/PracticeQuesAns.html', context=responseRecs)

def PracticeQuesView(request):
    form = PracticeQuesForm()
    fillform = PracticeQues.objects.all()
    if request.method == 'POST':
        form = PracticeQuesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return PracticeQuesAns(request)
        else:
            print("error...\n", form.errors)
            data = {"insertdata": fillform }
            form = PracticeQuesForm(initial=data)
    return render(request, 'Student/PracticeQues.html', {'insertform': fillform, 'form': form})
