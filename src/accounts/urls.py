from django.urls import path
from django.contrib.auth import login

from . views import register


app_name = 'accounts'

urlpatterns = [
    path('register/' , register , name='register')

]
