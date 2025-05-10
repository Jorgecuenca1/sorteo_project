from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rifa/<int:rifa_id>/', views.rifa_detalle, name='rifa'),
    path('reservar/<int:posicion_id>/', views.reservar_posicion, name='reservar_posicion'),
]
