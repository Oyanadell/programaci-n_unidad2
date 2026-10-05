from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(null=True)
    precio = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField()
    activo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ${self.precio}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Pedido(models.Model):
    fecha = models.DateField()
    pagado = models.BooleanField()

    # 1-N: Un cliente realiza muchos pedidos
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cliente")

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ["fecha"]

    def __str__(self):
        return f"{self.fecha}"
    
class Item(models.Model):
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="item")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, related_name="producto")

    class Meta:
        verbose_name_plural = "Items"
        ordering = ["cantidad"]

    def __str__(self):
        return f"{self.cantidad}"
