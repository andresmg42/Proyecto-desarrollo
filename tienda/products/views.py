from django.shortcuts import render
from django.shortcuts import HttpResponse

def adminCategorias(request):
    return render(request, "products/categoriasAdmin.html")

def adminVentas(request):
    return render(request, "products/adminVentas.html")

def adminProductos(request):
    return render(request, "products/productosAdmin.html")


# Create your views here.
