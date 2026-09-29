from django.db import models

# Model (El Modelo) = La Base de Datos. Aqui escribiras clases de Python que representaran el esqueleto 
# de tu informacion (class Libro). 

# 07_Django_Models_y_Panel_Admin.ipynb

# MATERIAL  >>> id, nombre, precio_gramo
class Material(models.Model):
    """Representa el material disponible para impresión 3D."""

    nombre = models.CharField(max_length=200)
    precio_gramo = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.nombre