from django.shortcuts import render, redirect, get_object_or_404 
from django.views.decorators.csrf import csrf_exempt
from .models import Institucion, Registro
from seminariosApp.form import formRegistro
from .serializers import RegistroSerializer, InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.generic import View
from django.http import Http404, JsonResponse

def index(request):
    return render(request, 'index.html')


# ==================== CRUD ====================
def crud(request):
    return render(request, 'listadoregistros.html', {})

# Listar
def listadoregistros(request):
    registros = Registro.objects.all()
    data =  {'registros': registros}
    return render(request, 'listadoregistros.html', data)

# Crear
def agregarregistro(request):
    form = formRegistro()
    if request.method == 'POST':
        print(request.POST)
        form = formRegistro(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form' : form}
    return render(request, 'crear.html', data)

# Eliminar
def eliminarregistro(request, id):
    reg = Registro.objects.get(id = id)
    reg.delete()
    return redirect('/listadoregistros')

# Actualizar
def actualizarregistro(request, id):
    reg = Registro.objects.get(id = id)
    form = formRegistro(instance=reg)
    if request.method == 'POST':
        form = formRegistro(request.POST, instance=reg)
        if form.is_valid() :
            form.save()
        return redirect('/listadoregistros')
    data = {'form' : form}
    return render(request, 'crear.html', data)


# ==================== Api  ====================
def listadoRegistro(request):
    registro = Registro.objects.all()
    data = {'registro': list(registro.values(
        'id',
        'nombre',
        'telefono',
        'institucion',
        'fecha_inscripcion',
        'hora_inscripcion',
        'estado',
        'observacion'
        ))}
    return JsonResponse(data)


@api_view(['GET'])
def registroDetalle(request, pk):
    try: 
        participante = Registro.objects.get(id = pk)
    except Registro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = RegistroSerializer(participante)
        return Response(serial.data)



# ==================== Class Based View  ====================
class RegistroListaB(APIView):
    def get(self, request):
        reg = Registro.objects.all()
        serial = RegistroSerializer(reg, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = RegistroSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistroDetalleB(APIView):
    def get_object(self, pk):
        try:
            return Registro.objects.get(id=pk)
        except Registro.DoesNotExist:
            return Http404

    def get(self, request, pk):
        reg = self.get_object(pk)
        serial = RegistroSerializer(reg)
        return Response(serial.data)
                
    def put(self, request, pk):
        reg = self.get_object(pk)
        serial = RegistroSerializer(reg, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        reg = self.get_object(pk)
        reg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ==================== Function Based View Institucion  ====================

@api_view (['GET', 'POST'])
def institucionLista(request):
    if request.method == 'GET':
        institucion = Institucion.objects.all()
        serial = InstitucionSerializer(institucion, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionSerializer.objects.all()
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucionDetalle(request, pk):
    try: 
        institucion = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializer(institucion)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(institucion, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
def carta(request):
    return render(request, 'carta.html', {})
