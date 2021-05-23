from django.urls import path,include
from .views import *

urlpatterns = [
    path("tipo1/populate", PopulateEstadisticasTipo1.as_view()),
    path("tipo1/get", EstadisticasTipo1API.as_view()),
]