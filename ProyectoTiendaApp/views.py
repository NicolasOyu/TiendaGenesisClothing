from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "ProyectoTiendaApp/home.html")

def informacion(request):

    return render(request, "ProyectoTiendaApp/informacion.html")

def tienda(request):

    return render(request, "ProyectoTiendaApp/tienda.html")

def contacto(request):

    return render(request, "ProyectoTiendaApp/contacto.html")
