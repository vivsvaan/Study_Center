
from django.conf.urls import url
from Trainer import views

app_name='Trainer'

urlpatterns = [
        url(r'^registration/', views.register, name='register'),
        url(r'^login/', views.user_login, name='user_login'),
        url(r'^Dashboard/', views.Dashboard, name='dashboard'),
]
