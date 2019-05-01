from django.shortcuts import render
from Trainer.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Trainer.models import Document, UserProfileInfo
# Create your views here.
def index(request):
    return render(request, 'Trainer/index.html')

def Dashboard(request, docRecs):

    return render(request, "Trainer/Dashboard.html", context=docRecs)

def register(request):
    registered=False

    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'Trainer/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse('index'))
    return render(request, 'Trainer/login.html', {})

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                record = UserProfileInfo.objects.get(user=user)
                userRec = {'record':record}
                userTopic = str(userRec['record'].topic)
                docrec = Document.objects.filter(topic=userTopic)
                docRecs = {'docrec':docrec}
                # return HttpResponseRedirect(reverse('index'))
                return render(request, "Trainer/Dashboard.html", context=docRecs)
            else:
                return HttpResponse("account not active")
        else:
            print("error....\nlogin failed")
            print("username: {} password: {}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request, 'Trainer/login.html', {})
