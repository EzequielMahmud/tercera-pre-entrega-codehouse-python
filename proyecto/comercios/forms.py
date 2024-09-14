from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from .models import Cliente, Ropa, Ventas, Talle

# -------------------------------------------------------------------------------------------------------- #

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {'nacimiento': forms.DateInput(attrs={'type': 'date'})}

# -------------------------------------------------------------------------------------------------------- #

class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = '__all__'

TalleFormSet = inlineformset_factory(Ropa, Talle, fields=('talle', 'stock'), extra=5)

# -------------------------------------------------------------------------------------------------------- #

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {'fecha_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'})}