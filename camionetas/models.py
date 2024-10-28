from django.db import models

class Objetos_Camionetas (models.Model):
    id_Objetos = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    camioneta_ID_Producto = models.IntegerField()
    cantidad = models.FloatField(default=0)

class Camionetas (models.Model):
    id_Camionetas = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 15, unique=True)
    