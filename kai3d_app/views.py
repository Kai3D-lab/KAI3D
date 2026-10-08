# UserCreationForm()  >>>  formulario  >>>  render(...)  >>>  registro.html

# GET  >>>  mostrar formulario vacio  >>>  Usario pulsa <Crear cuenta>  
# POST  >>>  recibe y valida los datos introducidos por el usuario

# 08_Django_Vistas_y_Templates.ipynb

# View (la vista) = El Cerebro Intermedio. 
# Las vistas reciben las peticiones del usuario, procesan los datos 
# y conectan la logica de Python con los Templates HTML.

from django.shortcuts import render, redirect

# Se utilizan los formularios de autenticacion integrados de Django para crear
# usuarios e iniciar sesion sin gestionar contraseñas manualmente.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistroUsuarioForm, ImpresionForm 
from .models import Impresion

import logging
logger = logging.getLogger("kai3d_app")

from .core.piezas import PiezaCliente, DatosPiezaInvalidosError


# Crea tus vistas aqui.
# kai3d_app/templates/kai3d_app/inicio.html

def inicio(request):
    """Muestra la pagina principal de KAI 3D."""
    return render(request, 'kai3d_app/inicio.html')

# Crear la vista registro
# 08_Django_Vistas_y_Templates.ipynb
# A) CREATE (Crear Libro mediante Frontend)
# La vista debe manejar tanto la entrega del formulario vacio (GET) como la 
# recepcion de datos rellenos (POST):

def registro(request):
    """Muestra el formulario para crear una cuenta de usuario."""

    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)

        # Comprueba que los datos introducidos son validos
        if formulario.is_valid():
            usuario = formulario.save()

            # Inicia sesion automaticamente al usuario que se acaba de registrar
            login(request, usuario)

            # Despues de crear la cuenta, vuelve a la pagina principal
            return redirect('inicio')
    else:
        formulario = RegistroUsuarioForm()

    # Envia el formulario de Python and HTML
    return render(
        request, 
        'kai3d_app/registro.html', 
        {'formulario': formulario})

# Crear la vista para iniciar sesion

# KAI 3D necesita identificar al usuario para asociar sus futuros pedidos,
# impresiones a su cuenta

def iniciar_sesion(request):
    """Muestra el formulario para iniciar sesion."""

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)

        # Comprueba que el usuario y la contraseña son correctos
        if formulario.is_valid():
            usuario = formulario.get_user()

            # Inicia la sesión del usuario
            login(request, usuario)

            # Coprueba si hay una URL de redireccionamiento despues de iniciar sesion
            siguiente = request.GET.get('next')
            if siguiente:
                return redirect(siguiente)
            return redirect('inicio')

    else:
        formulario = AuthenticationForm()

    return render(request, 'kai3d_app/login.html', {'formulario': formulario})

# Crear la vista para cerrar sesión

# Cierra la sesion del usuario autenticado.
def cerrar_sesion(request):
    """Cierra la sesión del usuario."""

    logout(request)

    return redirect('inicio')


# Crear una nueva impresion 

@login_required

def crear_impresion(request):
    """Procesa una solicitud de impresion 3D."""
    # Pseudocodigo:
    # 1. Recibir los datos y el archivo STL del usuario.
    # 2. Validar los datos del formulario.
    # 3. Asociar el pedido con el usuario autenticado.
    # 4. Crear un objeto PiezaCliente.
    # 5. Calcular el peso y el coste del material.
    # 6. Si hay un error, mostrarlo y registrar una advertencia.
    # 7. Si todo es correcto, guardar el pedido en la base de datos.

    if request.method == 'POST':
        formulario = ImpresionForm(request.POST, request.FILES)

        if formulario.is_valid():
            # Todavia no guarda en la base de datos, solo crea un objeto Impresion en memoria
            impresion = formulario.save(commit=False)

            # Asocia la impresion con el usuario autenticado
            impresion.usuario = request.user

            try:
                # Crear el objeto POO con los datos del pedido
                pieza = PiezaCliente(
                    impresion.fichero.name,
                    impresion.cantidad,
                    impresion.volumen_cm3,
                    impresion.material.densidad,
                    impresion.material.precio_gramo)

                # Calcular peso y coste utilizando el Core POO
                impresion.peso_estimado = pieza.calcular_peso()
                # Calcular el coste del material utilizando el Core POO
                impresion.coste_material = round(pieza.calcular_coste(), 2)

            except DatosPiezaInvalidosError as error:
                logger.warning("Datos de pieza invalidos: %s", error)
                formulario.add_error(None, str(error))
            else:        
                # Guardar el pedido solo si el calculo fue correcto
                impresion.save()

                # Log de la creacion de la impresion
                logger.info("Nuevo pedido creado correctamente.")

                return redirect('mis_pedidos')
    else:
        formulario = ImpresionForm()

    return render(
        request, 
        'kai3d_app/crear_impresion.html', 
        {'formulario': formulario})


# Mostrar los pedidos del usuario 

@login_required

def mis_pedidos(request):
    """Muestra los pedidos del usuario autenticado, del mas reciente al mas antiguo."""

    # Solo busca las impresiones asociadas al usuario conectado
    impresiones = Impresion.objects.filter(usuario=request.user).order_by("-fecha")

    return render(
        request, 
        'kai3d_app/mis_pedidos.html', 
        {'impresiones': impresiones})   
