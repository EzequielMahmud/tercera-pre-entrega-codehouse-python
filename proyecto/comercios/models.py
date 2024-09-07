from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    domicilio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        if self.domicilio is not None:
            return f"{self.apellido.capitalize()}, {self.nombre.capitalize()}, {self.celular}, {self.domicilio}."
        else:
            return f"{self.apellido.capitalize()}, {self.nombre.capitalize()}, {self.celular}."
            
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Ropa(models.Model):
    class TiposRopa(models.TextChoices):
        REMERA = 'remera', 'Remera'
        PANTALON = 'pantalon', 'Pantalon'
        CAMPERA = 'campera', 'Campera'

    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=250, blank=True, null=True)
    precio = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=TiposRopa, default=TiposRopa.REMERA)

    def __str__(self) -> str:
        return f"{self.get_tipo_display()}, {self.nombre}"
    
    def hay_stock(self):
        """Verifica si hay stock disponible en algún talle."""
        return self.talles.filter(stock__gt=0).exists()
    
    class Meta:
        verbose_name = "Ropa"
        verbose_name_plural = "Ropa"

class Talle(models.Model):
    class Talles(models.TextChoices):
        S = 's', 'S'
        M = 'm', 'M'
        L = 'l', 'L'
        XL = 'xl', 'XL'
        XXL = 'xxl', 'XXL'

    ropa = models.ForeignKey(Ropa, on_delete=models.CASCADE, related_name='talles')
    talle = models.CharField(max_length=3, choices=Talles.choices)  # vincular los talles y definir cuanto stock hay en cada talle para después poder hacer sumas o restas al comprar o cancelar un pedida.
    stock = models.PositiveIntegerField(default=0)  # stock por talle, default 0

    def __str__(self):
        return f"Talle: {self.get_talle_display()}, Stock: {self.stock}"

    class Meta:
        verbose_name = "Talle"
        verbose_name_plural = "Talles"


class Ventas(models.Model):
    class Estado(models.TextChoices): #uso choices para seleccionar el estado
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROCESO = 'EN_PROCESO' 'En Proceso'
        COMPLETADO = 'COMPLETADO', 'Completado'
        CANCELADO = 'CANCELADO', 'Cancelado'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ropa = models.ForeignKey(Ropa, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=250, blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)

    def __str__(self) -> str:
        return f"Pedido de {self.ropa} para {self.cliente.nombre} {self.cliente.apellido}"
    
    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "Ventas"