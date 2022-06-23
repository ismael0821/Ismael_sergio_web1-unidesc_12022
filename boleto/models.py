from django.db import models

class Boleto(models.Model):

    codClientes = models.CharField(max_length=100)
    nomeClientes = models.CharField(max_length=100)


    def __str__(self):
        return self.Boleto