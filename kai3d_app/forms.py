from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Impresion

import logging
logger = logging.getLogger("kai3d_app")

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label="Correo electrónico")
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ImpresionForm(forms.ModelForm):

    def clean_fichero(self):
        """Validar que el archivo tenga extensión .stl."""
        fichero = self.cleaned_data.get('fichero')

        # Validar que el archivo tenga extensión .stl
        if fichero and not fichero.name.lower().endswith('.stl'):
            # Registrar las cargas de archivos STL rechazadas
            logger.warning("Archivo rechazado: formato no valido.")
            raise forms.ValidationError(
                "El archivo debe tener formato .stl")
        
        return fichero

    def clean_volumen_cm3(self):
        """Validar que el volumen sea mayor que cero."""
        volumen = self.cleaned_data.get('volumen_cm3')

        if volumen is None or volumen <= 0:
            raise forms.ValidationError(
                "El volumen debe ser mayor que cero")

        return volumen
    
    class Meta:
        model = Impresion
        fields = ['fichero', 'material', 'volumen_cm3', 'cantidad', 'notas']

    def clean_cantidad(self):
        """Validar que la cantidad sea mayor que cero."""
        cantidad = self.cleaned_data.get('cantidad')

        # Validar que la cantidad sea mayor que cero
        if cantidad is None or cantidad < 1:
            raise forms.ValidationError(
                "La cantidad debe ser mayor que cero")

        return cantidad


