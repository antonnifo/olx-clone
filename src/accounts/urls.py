from django.urls import path
from django.contrib.auth import login

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', login, name='login'),

]