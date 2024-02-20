from django.urls import path
from .views import *



urlpatterns = [
    path('/alunos', alunos, name = 'alunos'),
]
