"""
URL configuration for kai3d_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Añadimos path porque creamos otro archivo URL  kai3d_app >>> urls.py
from django.urls import include, path # path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Browser >>> kai3d_core/urls.py >>> is it/admin/? >>> 
    # yes >>> Django Admin
    # no >>> kai3d_app/urls.py
    path('', include('kai3d_app.urls')), 
]

