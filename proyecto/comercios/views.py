from django.shortcuts import render
from .models import Cliente, Ropa, Ventas

# Create your views here.
def index(request):
    return render(request, 'comercios/index.html')

def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, 'comercios/cliente_list.html', context)

# def cliente_create(request):
#     query = Cliente.objects.all()
#     context = {"object_list": query}
#     return render(request, 'comercios/cliente_list.html', context)

def ropa_list(request):
    query = Ropa.objects.all()
    context = {"object_list": query}
    return render(request, 'comercios/ropa_list.html', context)

# def ropa_create(request):
#     query = Ropa.objects.all()
#     context = {"object_list": query}
#     return render(request, 'comercios/ropa_list.html', context)


def ventas_list(request):
    query = Ventas.objects.all()
    context = {"object_list": query}
    return render(request, 'comercios/ventas_list.html', context)