from django.contrib import admin
from .models import Cliente, Ropa, Ventas

# admin.site.register(Cliente)
# admin.site.register(Ropa)
# admin.site.register(Ventas)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "celular")
    list_filter = ("nombre", "apellido", "celular")
    search_fields = ("apellido", "nombre", "celular")
    ordering = ("apellido", "nombre")

@admin.register(Ropa)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock")
    list_filter = ("stock",)
    search_fields = ("nombre",)
    ordering = ("nombre",)

@admin.register(Ventas)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "ropa", "estado", "fecha_solicitud", "fecha_entrega")
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("cliente__nombre", "ropa__nombre")
    ordering = ("-fecha_entrega",)
    date_hierarchy = "fecha_solicitud"