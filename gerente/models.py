from django.db import models

class Gerente(models.Model):

    comissao = models.IntegerField(max_length=100)

    def __str__(self):
        return self.calcular_Salario