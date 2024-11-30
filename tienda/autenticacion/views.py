from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "autenticacion/login.html")

def register(request):
    return render(request, "autenticacion/register.html")

def adminUsuarios(request):
    return render(request, "autenticacion/usuariosAdmin.html")