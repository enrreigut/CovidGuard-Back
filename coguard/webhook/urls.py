from django.urls import path
from .views import *

urlpatterns = [
    path("webhook/", WebhookEstadisticasTipo1API.as_view()),
]
