from django.conf.urls import url
from Trainer import views
app_name = 'Trainer'
urlpatterns = [
    url(r'^login/', views.TrainerFormView, name='login'),
    url(r'^Dashboard/', views.Dashboard, name='dashboard'),
    url(r'^Profile/', views.Profile, name='profile'),
]
