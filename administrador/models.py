from django.db import models

class Administrador(models.Model):

    def __str__(self):
        return self.calcular_Salario