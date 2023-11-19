from rest_framework import serializers
from rest_framework.authtoken.models import Token
from herramientasweb_api.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

#SERIALIZER DE MATERIAS
class MateriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nrc = serializers.CharField(required=True)
    nombre_materia = serializers.CharField(required=True)
    seccion = serializers.CharField(required=True)
    dias = serializers.CharField(required=True)
    horai = serializers.TimeField(required=True)
    horaf = serializers.TimeField(required=True)
    salon = serializers.CharField(required=True)
    carrera = serializers.CharField(required=True)
    


    
#FIN DE SERIALIZER MATERIAS

class ProfilesSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = "__all__"
class ProfilesAllSerializer(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = '__all__'
        depth = 1
