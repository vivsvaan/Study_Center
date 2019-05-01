
from django.conf.urls import url
from Student import views

app_name='Student'

urlpatterns = [
        url(r'^registration/', views.register, name='register'),
        url(r'^login/', views.user_login, name='user_login'),
        url(r'^Dashboard/', views.Dashboard, name='dashboard'),
        url(r'^index/', views.index, name='index'),
]
