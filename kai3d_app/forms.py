from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Impresion


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label="Correo electrónico")
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ImpresionForm(forms.ModelForm):
    class Meta:
        model = Impresion
        fields = ['fichero', 'material', 'cantidad', 'notas']


