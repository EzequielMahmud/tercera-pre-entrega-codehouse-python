from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}, {self.celular}, {self.domicilio}."


class Ropa(models.Model):    
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=250, blank=True, null=True)
    talle = models.TextField(max_length=25, blank=True, null=True)
    precio = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    stock = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre


class Ventas(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROCESO = 'EN_PROCESO' 'En Proceso'
        COMPLETADO = 'COMPLETADO', 'Completado'
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ropa = models.ForeignKey(Ropa, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=250, blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)

    def __str__(self) -> str:
        return f"Pedido de {self.ropa} para {self.cliente.nombre}"