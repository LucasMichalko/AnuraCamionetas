from django.http import HttpResponse
from django.shortcuts import render
from camionetas.models import Camionetas, Objetos_Camionetas

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

def Create_Objects (request):
    if request.method == 'GET':
        Listar_Stock = Objetos_Camionetas.objects.all
        context = {
        "Listar_Stock":Listar_Stock,
        }
        return render(request, "Alta_Productos.html", context=context)

    elif request.method == 'POST':
        listar_stock = Objetos_Camionetas.objects.all()
        listar_camionetas = Camionetas.objects.all()
        
        name = request.POST.get('name')
        for camioneta in listar_camionetas:
                # Aquí usamos el ID de cada camioneta
            Objetos_Camionetas.objects.create(
                name=name,
                camioneta_ID_Producto = camioneta.id_Camionetas  # O camioneta, si es un ForeignKey
            )

        context = {
            "listar_stock": listar_stock,
            "listar_stock": listar_stock
        }
        return render(request, "Alta_Productos.html", context=context)