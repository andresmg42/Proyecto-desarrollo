from django.shortcuts import render
from django.shortcuts import HttpResponse


def adminPedidos(request):
    return render(request, "pedidos/adminPedidos.html")

# Create your views here.
