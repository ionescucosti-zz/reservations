from django.urls import path
from . import views


urlpatterns = [
    path('reservations/', views.reservations.as_view(), name='reservations'),
]
