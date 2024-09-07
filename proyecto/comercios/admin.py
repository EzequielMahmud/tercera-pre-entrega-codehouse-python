from django.contrib import admin
from .models import Cliente, Ropa, Ventas, Talle

# admin.site.register(Cliente)
# admin.site.register(Ropa)
# admin.site.register(Ventas)
class TalleInline(admin.TabularInline):
    model = Talle
    extra = 1

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "celular")
    list_filter = ("nombre", "apellido", "celular")
    search_fields = ("apellido", "nombre", "celular")
    ordering = ("apellido", "nombre")

@admin.register(Ropa)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "hay_stock")
    # list_filter = ("stock",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
    inlines = [TalleInline]

@admin.register(Ventas)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "ropa", "estado", "fecha_solicitud", "fecha_entrega")
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("cliente__nombre", "ropa__nombre")
    ordering = ("-fecha_entrega",)
    date_hierarchy = "fecha_solicitud"

@admin.register(Talle)
class TalleAdmin(admin.ModelAdmin):
    list_display = ("ropa", "get_talle_display", "stock")
    list_filter = ("ropa", "talle")
    search_fields = ("ropa__nombre",)