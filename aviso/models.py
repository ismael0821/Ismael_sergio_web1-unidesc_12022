from django.db import models

class Aviso(models.Model):

    matricula_avi = models.IntegerField(max_length=100)
    assunto_avi = models.CharField(max_length=100)
    data_avi = models.DateField(max_length=100)

    def __str__(self):
        return self.Incluir_Aviso

    def __str__(self):
        return self.Consultar_Aviso

    def __str__(self):
        return self.Remover_Aviso