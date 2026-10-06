from django.db import models
from django.conf import settings

# Model (El Modelo) = La Base de Datos. Aqui escribiras clases de Python que representaran el esqueleto 
# de tu informacion (class Libro). 

# 07_Django_Models_y_Panel_Admin.ipynb
# usuario  1:N  impresion  N:1  material

# MATERIAL  >>> id, nombre, precio_gramo
class Material(models.Model):
    """Representa el material disponible para impresión 3D."""

    nombre = models.CharField(max_length=200)
    precio_gramo = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.nombre

# Impresion usa Material  >>> ForeignKey
class Impresion(models.Model):

    # Si el usuario elimina su cuenta, elimina su historia de ordenes
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)

    # No eliminar material 
    material = models.ForeignKey(
        Material, 
        on_delete=models.PROTECT)

    # Archivo STL - fichero
    fichero = models.FileField(upload_to="impresiones/")

    # Valores se calculan despues de revisar el archivo STL 
    volumen_cm3 = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        null=True,
        blank=True)

    peso_estimado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True)

    cantidad = models.PositiveIntegerField(default=1)

    # Informacion adicional escrita por el usuario
    notas = models.TextField(blank=True)

    # Precio calculado de la impresion
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=True,
        blank=True)

    # Django guarda el pedido automaticamente
    fecha = models.DateTimeField(auto_now_add=True)

    # Estado del pedido
    estado = models.CharField(
        max_length=30, 
        default='Pendiente')

    def __str__(self):
        return f"Impresion {self.id} - {self.usuario}"

