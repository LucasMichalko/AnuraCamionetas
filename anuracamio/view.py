from django.http import HttpResponse
from django.shortcuts import render
from camionetas.models import Camionetas, Objetos_Camionetas

def index (request):
    Listar_camionetas = Camionetas.objects.all
    Listar_stock = Objetos_Camionetas.objects.all()
    context = {
        "Listar_camionetas":Listar_camionetas,
        "Listar_stock": Listar_stock
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
        Listar_stock = Objetos_Camionetas.objects.all()
        Listar_camionetas = Camionetas.objects.all()
        context = {
            "Listar_stock": Listar_stock,
            "Listar_camionetas":Listar_camionetas,
        }
        return render(request, "Alta_Productos.html", context=context)

    elif request.method == 'POST':
        Listar_stock = Objetos_Camionetas.objects.all()
        Listar_camionetas = Camionetas.objects.all()
        
        name = request.POST.get('name')
        for camioneta in Listar_camionetas:
               
            Objetos_Camionetas.objects.create(
                name=name,
                camioneta_ID_Producto = camioneta.id_Camionetas
            )  

        context = {
            "Listar_stock": Listar_stock,
            "Listar_camionetas":Listar_camionetas,
        }
        return render(request, "Alta_Productos.html", context=context)
    
def Stock_Camionetas(request,ID_camio):
    Listar_camionetas = Camionetas.objects.all
    Listar_stock = Objetos_Camionetas.objects.all()
    context = {
        "Listar_camionetas":Listar_camionetas,
        "Listar_stock": Listar_stock
    }
    return render (request, "Stock_Camionetas.html", context=context)
