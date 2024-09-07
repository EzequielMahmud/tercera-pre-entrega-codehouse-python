from django import forms
from django.forms import inlineformset_factory
from .models import Cliente, Ropa, Ventas, Talle

# -------------------------------------------------------------------------------------------------------- #

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = '__all__'

# -------------------------------------------------------------------------------------------------------- #

class RopaForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = '__all__'

TalleFormSet = inlineformset_factory(Ropa, Talle, fields=('talle', 'stock'), extra=5)

# -------------------------------------------------------------------------------------------------------- #

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ropa
        fields = '__all__'