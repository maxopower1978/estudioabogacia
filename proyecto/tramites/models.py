from django.db import models


class TipoDeTramite(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Tramite(models.Model):
    nombre = models.CharField(max_length=50)
    juzgado = models.TextField(max_length=50)
    TipoDeTramite_origen_id = models.ForeignKey(
        TipoDeTramite, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.nombre} es un tipo de trámite {self.TipoDeTramite_origen_id} y se tramita en el juzgado {self.juzgado}"
