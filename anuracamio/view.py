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
        "Listar_stock": Listar_stock,
        "ID_camio": ID_camio,
    }
    return render (request, "Stock_Camionetas.html", context=context)

def update_quantity(request, product_id):
    # Obtenemos las listas necesarias para el contexto
    Listar_camionetas = Camionetas.objects.all()
    Listar_stock = Objetos_Camionetas.objects.all()

    context = {
        "Listar_camionetas": Listar_camionetas,
        "Listar_stock": Listar_stock,
        "product_id": product_id,
    }

    if request.method == 'POST':
        # Obtenemos el cambio en cantidad (-1 o +1)
        change = int(request.POST.get('change', 0))
        
        # También obtenemos el nombre del producto, si está disponible
        product_name = request.POST.get('product_name', None)

        # Filtramos los productos por ID
        productos = Objetos_Camionetas.objects.filter(camioneta_ID_Producto=product_id)

        # Si también recibimos el nombre del producto, añadimos este filtro
        if product_name:
            productos = productos.filter(name=product_name)

        # Iteramos sobre los productos encontrados y actualizamos su cantidad
        for producto in productos:
            producto.cantidad = max(producto.cantidad + change, 0)  # Evitamos cantidades negativas
            producto.save()

    # Renderizamos el template con el contexto actualizado
    return render(request, "Stock_Camionetas.html", context=context)



