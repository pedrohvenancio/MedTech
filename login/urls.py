from django.urls import path
from login.views import index
from login.views import login

urlpatterns = [
    path('', index),
    path('login/autenticacao/', login, name='login'),
]