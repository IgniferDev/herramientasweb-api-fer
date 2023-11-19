from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from herramientasweb_api.serializers import *
from herramientasweb_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json

#de aqui para abajo funciones, esas son como yo vea
#POST GET PUT DELETE (por cada clase creada)

#PARA TABLA DE MATERIAS ATENCION REVISAR PRECAUCION
class MateriasAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materias = Materias.objects.filter().order_by("id") #NO SE AGREGA NADA EN EL () DE FILTER PORQUE NO ES POR USUARIOS, SOLO SE FILTRA POR ID Y YA
        lista = MateriaSerializer(materias, many=True).data

        return Response(lista, 200)


class MateriasView(generics.CreateAPIView):

    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):#estructura general de la funcion
        materi = get_object_or_404(Materias, id = request.GET.get("id"))
        materi = MateriaSerializer(materi, many=False).data #SE DECLARA ASI PARA EVITAR PROBLEMAS CON NOMBRE COMO "materia" o "materias" ERROR MIO POR PARTE DE ESCOGER NOMBRE VARIABLES JSON Y FUNCIONES
        return Response(materi, 200)

    
    @transaction.atomic
    def post(self, request, *args, **kwargs):#estructura basica
        
        mat = MateriaSerializer(data=request.data)# el serializer va en el serializer de pyi o el extension
        if mat.is_valid():
            
          
            materia = Materias.objects.create(  nrc=request.data["nrc"],
                                                nombre_materia=request.data["nombre_materia"],
                                                seccion=request.data["seccion"],
                                                dias=request.data["dias"],
                                                horai=request.data["horai"],
                                                horaf=request.data["horaf"],
                                                salon=request.data["salon"],
                                                carrera=request.data["carrera"])
            materia.save()

            return Response({"materia_created_id": materia.id}, 201)
    
        return Response(mat.errors ,status=status.HTTP_400_BAD_REQUEST)
    

class MateriasViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        mate = get_object_or_404(Materias, id=request.data["id"])
        mate.nrc = request.data["nrc"]
        mate.nombre_materia = request.data["nombre_materia"]
        mate.seccion = request.data["seccion"]
        mate.dias = request.data["dias"]
        mate.horai = request.data["horai"]
        mate.horaf = request.data["horaf"]
        mate.salon = request.data["salon"]
        mate.carrera = request.data["carrera"]
        mate.save()#SE GUARDA A BASE DE DATOS EN DJANGO CON UN .save()
        ma = MateriaSerializer(mate, many=False).data#para dar estructura en formato json
        return Response(ma,200)
    #AL FIN Y AL CABO SON VARIABLES SOLO SON PARA SU USO PERO TENER CUIDADO CON LOS NOMBRES

    def delete(self, request, *args, **kwargs):
        profile = get_object_or_404(Materias, id=request.GET.get("id"))
        try:
            profile.delete()#SE PONE UNICAMENTE DELETE NO USER.DELETE O MATERIA.DELETE
            #PORQUE NO TIENE LLAVE FORANEA ENTONCES SE ELIMINA DIRECTAMENTE
            #AL ELIMINAR LA LLAVE FORANEA TAMBIEN SE ELIMINA NO RELACIONADO A ESTA
            return Response({"details": "Materia ELIMINADA"}, 200)
        except Exception as e:
            return Response({"details": "ALGO OCURRIO"}, 400)