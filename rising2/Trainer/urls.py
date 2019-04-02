
from django.conf.urls import url
from Trainer import views

app_name='Trainer'

urlpatterns = [
        url(r'^registration/', views.register, name='register'),
        url(r'^user_login/', views.user_login, name='user_login'),
]
