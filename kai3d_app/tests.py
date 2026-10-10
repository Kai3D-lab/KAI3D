from django.test import SimpleTestCase

from .core.piezas import PiezaCliente

from .core.piezas import PiezaCliente, DatosPiezaInvalidosError

from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import ImpresionForm

from django import forms

from django.test import TestCase

from django.urls import reverse

class PruebasPiezaCliente(SimpleTestCase):
    """Pruebas de los cálculos de piezas para impresión 3D."""

    def test_calcular_peso(self):
        """Comprueba que el peso se calcula correctamente."""
        pieza = PiezaCliente(
            nombre="Pieza de prueba",
            cantidad=2,
            volumen_cm3=10,
            densidad=1.24,
            precio_gramo=0.05,
        )

        self.assertAlmostEqual(pieza.calcular_peso(), 12.4)
    
    def test_calcular_coste(self):
        """Comprueba el coste total del material para dos piezas."""
        pieza = PiezaCliente(
            nombre="Pieza de prueba",
            cantidad=2,
            volumen_cm3=10,
            densidad=1.24,
            precio_gramo=0.05,
        )

        self.assertAlmostEqual(pieza.calcular_coste(), 1.24)

    def test_volumen_negativo(self):
        """Comprueba que no se permita un volumen negativo."""
        with self.assertRaises(DatosPiezaInvalidosError):
            PiezaCliente(
                nombre="Pieza de prueba",
                cantidad=2,
                volumen_cm3=-10,
                densidad=1.24,
                precio_gramo=0.05,
            )

    def test_cantidad_cero(self):
        """Comprueba que no se permita una cantidad igual a cero."""
        with self.assertRaises(DatosPiezaInvalidosError):
            PiezaCliente(
                nombre="Pieza de prueba",
                cantidad=0,
                volumen_cm3=10,
                densidad=1.24,
                precio_gramo=0.05,
            )


class PruebasFormularioImpresion(SimpleTestCase):
    """Pruebas de validacion del formulario de impresion."""

    def test_rechazar_archivo_pdf(self):
        """Comprueba que el formulario rechace archivos que no sean STL."""
        archivo = SimpleUploadedFile(
            "documento.pdf",
            b"contenido de prueba",
        )

        formulario = ImpresionForm()

        with self.assertRaises(forms.ValidationError):
            formulario.cleaned_data = {"fichero": archivo}
            formulario.clean_fichero()


    def test_aceptar_archivo_stl(self):
        """Comprueba que se acepte un archivo con extensión STL."""
        archivo = SimpleUploadedFile(
            "pieza.stl",
            b"contenido de prueba",
        )

        formulario = ImpresionForm()
        formulario.cleaned_data = {"fichero": archivo}

        resultado = formulario.clean_fichero()

        self.assertEqual(resultado, archivo)


    def test_rechazar_volumen_cero(self):
        """Comprueba que el formulario rechace un volumen igual a cero."""
        formulario = ImpresionForm()
        formulario.cleaned_data = {"volumen_cm3": 0}

        with self.assertRaises(forms.ValidationError):
            formulario.clean_volumen_cm3()


class PruebasPermisos(TestCase):
    """Pruebas de acceso a las vistas protegidas."""

    def test_mis_pedidos_requiere_login(self):
        """Comprueba que un visitante no pueda acceder a sus pedidos."""
        respuesta = self.client.get(reverse("mis_pedidos"))

        self.assertEqual(respuesta.status_code, 302)
        self.assertIn("/login/", respuesta.url)
