from django.shortcuts import render

# Create your views here.

def inicio(request):
    """Muestra la pagina principal de KAI 3D."""
    return render(request, 'kai3d_app/inicio.html')

