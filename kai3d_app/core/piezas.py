"""Clases de la logica principal para las piezas de KAI 3D."""

class DatosPiezaInvalidosError(Exception):
    """Error cuando los datos de una pieza no son validos."""
    pass


class Pieza3D:
    """Representa una pieza basica dentro del sistema de KAI 3D."""

    # Atributos privados de la clase Pieza3D
    def __init__(self, nombre, cantidad):
        """Inicializa una pieza con su nombre y cantidad."""
        self.__nombre = nombre
        self.__cantidad = cantidad

    @property
    def nombre(self):
        """Devuelve el nombre de la pieza."""
        return self.__nombre

    @property
    def cantidad(self):
        """Devuelve la cantidad de la pieza."""
        return self.__cantidad

    def calcular_coste(self):
        """Calcula el coste de la pieza."""
        raise NotImplementedError("Este metodo debe ser implementado por subclases.")


class PiezaCliente(Pieza3D):
    """Inicializa una pieza y valida los datos para calcular su coste."""


# Pseudocodigo para validar los datos de una pieza:
# 1. Comprobar que la cantidad sea mayor que cero.
# 2. Comprobar que el volumen sea positivo.
# 3. Comprobar que la densidad sea positiva.
# 4. Comprobar que el precio por gramo no sea negativo.
# 5. Si algun dato es incorrecto, lanzar una excepcion.
# 6. Si todos son correctos, guardar los atributos.

    def __init__(
            self,
            nombre, 
            cantidad,
            volumen_cm3,
            densidad,
            precio_gramo):

        if cantidad < 1:
            raise DatosPiezaInvalidosError(
                "La cantidad de piezas debe ser mayor a 0.")

        if volumen_cm3 <= 0:
            raise DatosPiezaInvalidosError(
                "El volumen de la pieza debe ser mayor que 0 cm3.")

        if densidad <= 0:
            raise DatosPiezaInvalidosError(
                "La densidad del material debe ser mayor que cero.")

        if precio_gramo < 0:
            raise DatosPiezaInvalidosError(
                "El precio por gramo no puede ser negativo.")

        super().__init__(nombre, cantidad)

        self.__volumen_cm3 = volumen_cm3
        self.__densidad = densidad
        self.__precio_gramo = precio_gramo

    def calcular_peso(self):
        """Calcula el peso estimado a partir del volumen y la densidad."""
        return self.__volumen_cm3 * self.__densidad

    def calcular_coste(self):
        """Calcula el coste total segun el peso, material y cantidad."""

# Pseudocodigo para calcular el coste de la pieza:
# 1. Obtener el volumen y la densidad del material.
# 2. Calcular el peso estimado de la pieza.
# 3. Multiplicar el peso por el precio por gramo.
# 4. Multiplicar por la cantidad de piezas. 
# 5. Devolver el coste estimado. 

        peso_gramos = self.calcular_peso()

        return (
            peso_gramos 
            * self.__precio_gramo 
            * self.cantidad)


    