from django.shortcuts import render

from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "gestion/home.html")

def login(request):
    return render(request, "gestion/login.html")

def register(request):
    return render(request, "gestion/register.html")

def adminInicio(request):
    return render(request, "gestion/index.html")

def adminCategorias(request):
    return render(request, "gestion/categoriasAdmin.html")

def adminVentas(request):
    return render(request, "gestion/ventasAdmin.html")

def adminProductos(request):
    return render(request, "gestion/productosAdmin.html")

def adminUsuarios(request):
    return render(request, "gestion/usuariosAdmin.html")

def adminPedidos(request):
    return render(request, "gestion/pedidosAdmin.html")