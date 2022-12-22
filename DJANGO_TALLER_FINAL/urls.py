"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from seminariosApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('listadoregistros/', views.listadoregistros, name='listadoregistros'),
    path('agregarregistro/', views.agregarregistro, name='agregarregistro'),
    path('eliminar/<int:id>', views.eliminarregistro),
    path('actualizar/<int:id>', views.actualizarregistro, name='eliminarregistro'),
    # Api
    path('api/registro/', views.listadoRegistro, name='api'),
    path('api/registro/<int:pk>', views.registroDetalle),
    # Class View
    path('class/registro/', views.RegistroListaB.as_view(), name='registroListab'),
    path('class/registro/<int:pk>', views.RegistroDetalleB.as_view()),
    # Function Based View
    path('institucion/', views.institucionLista, name='institucion'),
    path('institucion/<int:pk>', views.institucionDetalle),
    path('carta/', views.carta, name='carta'),
]
