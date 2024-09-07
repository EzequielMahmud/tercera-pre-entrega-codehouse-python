# App Comercios:

# SUPERUSER: admin | 1234

1. Mi idea es crear una app en la que pueda gestionar un comercio de indumentaria que cuenta con: 
    - Remeras
    - Pantalones
    - Camperas

2. En models cree 3 clases:
    - Cliente
    - Ropa
    - Ventas
El precio de la ropa lo dejé en opcional porque si el producto no tiene stock, no se puede definir un precio adecuado. Entiendo también que podría estar con el último precio que tuvo, pero voy a tratar de que si no está disponible, diga sin stock.

3. ProductoRopa :
    - FK (Producto)
    - Talle
    - Color



Traté de hacerlo todo lo más real posible a como se vería una página de indumentaria para un cliente.
Dentro de la clase de  Ropa intenté meter talles y stock, con la particularidad de que es stock por cada talle, o sea, el stock de X remera en M, después en L, en XL, etc
Estuve un rato largo investigando como y finalmente lo logré y pude plasmarlo en ropa_create poniendo los formularios y 5 campos para agregar talles ya que en la base de datos puse talles del S al XXL

