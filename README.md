# KAI3D


***   Description del proyecto   ***

KAI 3D es una aplicacion web desarrollada con Python y Django para 
gestionar solicitudes de impresion 3D.

Los usuarios pueden registrarse, iniciar sesion y solicitar 
presupuesto de impresion mediante archivos STL.Para cada solicitud, 
el sistema calcula el peso estimado y el coste del material segun 
el volumen de la pieza, la densidad del material seleccionado y la 
cantidad solicitado.

La aplicacion utilizada programacion orientada a objetos para realizar 
los calculos, SQLite para almacenar la informacion y Django Admin para 
gestionar los pedidos y sus estados. 



***   Instalacion y ejecucion   ***

Para ejecutar KAI 3D en un ordenador con Python instalado:

1. Clonar el repositorio
    git clone https://github.com/Kai3D-lab/KAI3D.git
    cd KAI3D

2. Crear y activar un entorno virtual
    python -m venv env
    .\env\Scripts\Activate.ps1

3. Instalar las dependencias
    python -m pip install -r requirements.txt

4. Preparar la base de datos SQLite
    python manage.py migrate

5. Iniciar el servidor
    python manage.py renserver

Abrir en el navegador: 
    http://127.0.0.1:8000/

Para acceder al panel de administracion, primero se debe crear un superusuario:
    python manage.py createsuperuser

Despues, acceder a:
    http://127.0.0.1:8000/admin/

Desde el panel de administracion se pueden registrar los materiales disponibles 
para las solicitudes de impresion. 


***   Uso de la aplicacion   ***

* Usuarios
    Los usuarios pueden registrarse e iniciar sesion para solicitar 
    de impresion 3D.

Para crear una solicitud:
1. Acceder a la opcion de crear una impresion.
2. Subir un archivo STL.
3. Seleccionar el material disponible.
4. Introducir el volumen de la pieza en cm3, la cantidad y, si es necesario, algunas notas.
5. Enviar la solicitud.

El sistema calcula automáticamente el peso estimado de la pieza y el coste del material. 
Estos cálculos son orientativos y no representan el precio final de la impresión.

En Mis pedidos, cada usuario puede consultar sus solicitudes, el estado de cada 
pedido y el precio final cuando esté disponible.

* Administrador

Desde Django Admin, el administrador puede gestionar los materiales, consultar las 
solicitudes recibidas, actualizar sus estados y establecer el precio final de cada pedido.

El precio final se introduce manualmente, ya que puede incluir otros factores además 
del coste del material, como el tiempo de impresión y el uso de la máquina.


***   Programacion orientada a objectos (POO)   ***

La lógica de cálculo se encuentra en el archivo kai3d_app/core/piezas.py, separada de 
las vistas y los modelos de Django.

Se utilizan dos clases principales:

Pieza3D: Clase base que contiene los atributos privados __nombre y __cantidad. 
Incluye propiedades para consultar estos valores y un método calcular_coste() que debe 
implementarse en las clases derivadas.

PiezaCliente: Hereda de Pieza3D y permite calcular el peso y el coste del material de 
una solicitud de impresión.

* Calculos

El peso estimado se obtiene mediante:
    peso = volumen_cm3 * densidad

El coste total del material se calcula mediante:
    coste = peso * precio_gramo * cantidad

El peso correspondiente a una pieza y el coste incluye todas las unidades solicitadas.

* validacion y excepciones

La clase PiezaCliente comprueba que la cantidad, el volumen y la densidad sean mayores
que creo, y que el precio por gramo no sea negativo.

Cuando se detectan datos incorrectos, se utiliza la excepción personalizada 
DatosPiezaInvalidosError.

Las vistas de Django capturan esta excepción mediante try-except para mostrar el 
error sin interrumpir la aplicación.

El proyecto también utiliza logging para registrar solicitudes creadas y advertencias 
relacionadas con archivos no válidos en kai3d.log.