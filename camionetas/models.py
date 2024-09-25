from django.db import models

class Objetos_Camionetas (models.Model):
    name = models.CharField(max_length=30)
    camioneta_ID = models.IntegerField()
    cantidad = models.FloatField()

class Camionetas (models.Model):
    name = models.CharField(max_length = 15)
    