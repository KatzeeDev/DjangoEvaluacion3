from rest_framework import serializers
from .models import Registro, Institucion

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'
        
class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'       