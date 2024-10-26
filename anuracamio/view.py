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
    if request.method == 'GET':
        Listar_camionetas = Camionetas.objects.all
        context = {
        "Listar_camionetas":Listar_camionetas,
        }
        return render(request, "Alta_Camionetas.html", context=context)

    elif request.method == 'POST':
      Camionetas.objects.create(name = request.POST['name'])
      Listar_camionetas = Camionetas.objects.all
      context = {
        "Listar_camionetas":Listar_camionetas,
    }
    return render (request, "abm_camionetas.html", context=context)
        

def ABM_Camionetas(request):
    Listar_camionetas = Camionetas.objects.all
    context = {
        "Listar_camionetas":Listar_camionetas,
    }
    return render (request, "abm_camionetas.html", context=context)