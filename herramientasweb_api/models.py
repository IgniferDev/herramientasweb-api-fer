from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    matricula = models.CharField(max_length=255,null=True, blank=True)
    curp = models.CharField(max_length=255,null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento=models.DateTimeField(auto_now_add=False,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=255,null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del usuario "+self.usuario.first_name+" "+self.usuario.last_name
    
class Materias(models.Model):
    id = models.BigAutoField(primary_key=True)
    nrc = models.CharField(max_length=255,null=True, blank=True)
    nombre_materia = models.CharField(max_length=255,null=True, blank=True)
    seccion = models.CharField(max_length=255,null=True, blank=True)
    dias = models.CharField(max_length=255,null=True, blank=True)
    horai = models.TimeField(max_length=255,null=True, blank=True)
    horaf= models.TimeField(auto_now_add=False,null=True, blank=True)
    salon = models.CharField(max_length=255, null=True, blank=True)#SIEMPRE ANADIR MAX LENGHT A LOS CHAR FIELD
    carrera = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil de Materia "+self.mat.materia+" "+self.mat.carrera
