from django.urls import path,include
from .views import *

urlpatterns = [
    path("tipo1/get", EstadisticasTipo1API.as_view()),
]