from django.conf.urls import url
from Student import views
app_name = 'Student'
urlpatterns = [
    url(r'^login/', views.StudentFormView, name='login'),
    url(r'^Dashboard/', views.Dashboard, name='dashboard'),
    url(r'^PracticeQues.html/', views.PracticeQuesView, name='practiceques'),
    url(r'^PracticeQuesAns.html/', views.PracticeQuesAns, name='practicequesans'),
]
