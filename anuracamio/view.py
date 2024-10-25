from django.http import HttpResponse
from django.shortcuts import render
from camionetas.models import Camionetas

def index (request):
    Listar_camionetas = Camionetas.objects.all
    context = {
        "Listar_camionetas":Listar_camionetas,
    }
    return render(request, "index.html", context=context)

def Create_camionetas (request):
    new_camioneta = Camionetas.objects.create(name="071")
    return HttpResponse ("Creado")

def ABM_Camionetas(request):
    Listar_camionetas = Camionetas.objects.all
    context = {
        "Listar_camionetas":Listar_camionetas,
    }
    return render (request, "abm_camionetas.html", context=context)