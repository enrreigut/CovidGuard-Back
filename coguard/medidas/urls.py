from django.urls import path, include
from .views import *

urlpatterns = [
    path("tipo1/populate", MedidasAPI.as_view()),
]