# http://127.0.0.1:8000/registro/  >>>  views.registro  >>>  registro.html


from django.urls import path
from . import views


# 08_Django_Vistas_y_Templates.ipynb
# Conectamos nuestras vistas del CRUD en el archivo de rutas central urls.py
urlpatterns = [
    # Pagina principal
    path('', views.inicio, name='inicio'),

    # Pagina para crear una cuenta
    path('registro/', views.registro, name='registro'),
    # Pagina para iniciar sesion,

    path('login/', views.iniciar_sesion, name='login'),

    # Cerrar la sesión del usuario 
    path('logout/', views.cerrar_sesion, name='logout'),

    # Crear una nueva impresion
    path('crear-impresion/', views.crear_impresion, name='crear_impresion'),

    # ver los pedidos del usuario
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
]
