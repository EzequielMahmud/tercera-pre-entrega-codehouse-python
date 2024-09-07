from django.shortcuts import render, redirect 
from .models import Cliente, Ropa, Ventas
from .forms import ClienteForm, RopaForm, VentasForm, TalleFormSet

# Create your views here.
def index(request):
    return render(request, 'comercios/index.html')

# -------------------------------------------------------------------------------------------------------- #

def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, 'comercios/cliente_list.html', context)

def cliente_create(request):
    if request.method == 'GET':
        form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')

    return render(request, 'comercios/cliente_create.html', {"form": form})

# -------------------------------------------------------------------------------------------------------- #

def ropa_list(request):
    query = Ropa.objects.all()
    context = {"object_list": query}
    return render(request, 'comercios/ropa_list.html', context)

def ropa_create(request):
    if request.method == 'GET':
        form = RopaForm()
        formset = TalleFormSet()
    if request.method == 'POST':
        form = RopaForm(request.POST)
        formset = TalleFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            ropa = form.save()  # Guardar la prenda primero
            talles = formset.save(commit=False)  # No guardamos aún el formset

            # Asignar la prenda a cada talle y guardar
            for talle in talles:
                talle.ropa = ropa
                talle.save()

            return redirect('ropa_list')

    return render(request, 'comercios/ropa_create.html', {"form": form, "formset": formset})

# -------------------------------------------------------------------------------------------------------- #

def ventas_list(request):
    query = Ventas.objects.all()
    context = {"object_list": query}
    return render(request, 'comercios/ventas_list.html', context)

def ventas_create(request):
    if request.method == 'GET':
        form = VentasForm()
    elif request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas_list')
        else:
            print(form.errors)

    return render(request, 'comercios/ventas_create.html', {"form": form})

# -------------------------------------------------------------------------------------------------------- #
