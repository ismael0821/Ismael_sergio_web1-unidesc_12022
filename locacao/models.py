from django.db import models

class Locacao(models.Model):

    dataDesocupacao = models.DateField(max_length=100)
    periodo = models.DateField(max_length=100)
    formaGaratia = models.CharField(max_length=100)
    fiado = models.CharField(max_length=100)

    def __str__(self):
        return self.Locacao