from django.db import models

class Objetos_Camionetas (models.Model):
    name = models.CharField(max_length=30)
    camioneta_ID = models.IntegerField()
    cantidad = models.FloatField(default=0)

class Camionetas (models.Model):
    name = models.CharField(max_length = 15, unique=True)
    