from django.db import models


# Create your models here.
class Captura(models.Model):
    datoCapturado = models.CharField(max_length=200)

    def __str__(self):
        fila = "{0}"
        return fila.format(self.datoCapturado)