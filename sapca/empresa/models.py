from django.db import models
from usuario.models import CustomUser
# Create your models here.
class Empresa(models.model):
    usuario = models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    tipoId = models.CharField(max_length=20)
    numId = models.CharField(max_length=20)
    tipoPersona = models.CharField(max_length=10)#natuarl o juridica
    nombre = models.CharField(max_length=100)
    regimen = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    web = models.CharField(max_length=100)
    correo = models.EmailField(max_length=50)
    logo = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now=True)

class Sucursal(models.model):
    empresa = models.ForeignKey(Empresa,on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    creacion = models.DateTimeField(auto_now=True)

class Bodega(models.model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    altura = models.CharField(max_length=20)
    area = models.CharField(max_length=20)


