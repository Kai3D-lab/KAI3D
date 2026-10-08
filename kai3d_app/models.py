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

    densidad = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        default=1.240)  # Densidad en g/cm3, valor por defecto para PLA

    def __str__(self):
        """Devuelve el nombre del material."""
        return self.nombre

# Impresion usa Material  >>> ForeignKey
class Impresion(models.Model):
    """Representa una impresión 3D solicitada por un usuario."""

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

    # El usuario introduce el volumen;; el peso y coste se calculan en el Core POO 
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

    # Coste estimado del material, calculado por el Core POO
    coste_material = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True)

    cantidad = models.PositiveIntegerField(default=1)

    # Informacion adicional escrita por el usuario
    notas = models.TextField(blank=True)

    # Precio final establecido por el administrador, puede ser diferente al coste del material
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=True,
        blank=True)

    # Django guarda el pedido automaticamente
    fecha = models.DateTimeField(auto_now_add=True)

    # Estado del pedido
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En revision', 'En revision'),
        ('Presupuesto', 'Presupuesto'),
        ('Listo para recoger', 'Listo para recoger'),
        ('Recogido', 'Recogido'),
        ('Cancelado', 'Cancelado'),
    ]

    # Estado del pedido, por defecto es Pendiente
    estado = models.CharField(
        max_length=30, 
        choices=ESTADOS,
        default='Pendiente')

    def __str__(self):
        """Devuelve el identificador del pedido y su usuario."""
        return f"Impresion {self.id} - {self.usuario}"

