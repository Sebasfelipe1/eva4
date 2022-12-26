from django.db import models

# Create your models here.


     
class PersonalRRHH(models.Model):
     nombre_personal = models.CharField(max_length=20)
     apellido_parterno = models.CharField(max_length=20)
     apellido_materno = models.CharField(max_length=20)
     rut = models.CharField(max_length=10)
     sector = models.CharField(max_length=20)
     seccion = models.CharField(max_length=20)
     
     def __str__(self):
          return str(self.nombre_personal)
     

     
class Auto(models.Model):
     marca_auto = models.CharField(max_length=50)
     ruedas = models.CharField(max_length=2)
     puertas = models.CharField(max_length=2)
     patente = models.CharField(max_length=10)
     dueño_auto = models.CharField(max_length=50)
     rut_dueño = models.CharField(max_length=10)
     
     def __str__(self):
          return self.marca_auto

class Cliente(models.Model):
     id = models.IntegerField(primary_key=True)
     nombre_cliente = models.CharField(max_length=20)
     apellidoP_cliente = models.CharField(max_length=20)
     apellidoM_cliente = models.CharField(max_length=20)
     rut = models.CharField(max_length=10)
     edad = models.CharField(max_length=10)
     telefono = models.CharField(max_length=13)
     nombre_personal = models.ForeignKey(PersonalRRHH, null=True, blank=True, on_delete=models.CASCADE)
     marca_auto = models.ForeignKey(Auto, null=True, blank=True, on_delete=models.CASCADE)
     
     
     
     