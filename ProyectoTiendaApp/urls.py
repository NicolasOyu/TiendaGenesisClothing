from django.urls import path
from ProyectoTiendaApp import views

urlpatterns = [
    path('', views.home, name = "Inicio"),
    path('informacion', views.informacion, name = "Informacion"),
    path('tienda', views.tienda, name = "Tienda"),
    path('contacto', views.contacto, name = "Contacto"),
]
