# UserCreationForm()  >>>  formulario  >>>  render(...)  >>>  registro.html
# User visits /registro/  >>>  GET  >>>  show empty form  >>>  User presses Crear cuenta  >>>  POST  >>>  receive what they typed

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Crea tus vistas aqui.
def inicio(request):
    """Muestra la pagina principal de KAI 3D."""
    return render(request, 'kai3d_app/inicio.html')

# Crear la vista registro
def registro(request):
    """Muestra el formulario para crear una cuenta de usuario."""

    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        # Comprueba que los datos introducidos son validos
        if formulario.is_valid():
            formulario.save()

            # Despues de crear la cuenta, vuelve a la pagina principal
            return redirect('inicio')
    else:
        formulario = UserCreationForm()

    return render(
        request,
        'kai3d_app/registro.html', # Envia el formulario de Python and HTML
        {'formulario': formulario}
    )

# Crear la vista para iniciar sesion
def iniciar_sesion(request):
    """Muestra el formulario para iniciar sesion."""

    if request.method == 'POST':
        formulario = AuthenticationForm(
            request,
            data=request.POST)

        # Comprueba que el usuario y la contraseña son correctos
        if formulario.is_valid():
            usuario = formulario.get_user()

            # Inicia la sesión del usuario
            login(request, usuario)

            return redirect('inicio')

    else:
        formulario = AuthenticationForm()

    return render(
        request,
        'kai3d_app/login.html',
        {'formulario': formulario}
    )

# Crear la vista para cerrar sesión
def cerrar_sesion(request):
    """Cierra la sesión del usuario."""

    logout(request)

    return redirect('inicio')

