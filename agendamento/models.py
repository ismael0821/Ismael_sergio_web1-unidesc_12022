from django.db import models

class Agendamento(models.Model):

    dia = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.incluir_Agendamento
    def __str__(self):
        return self.consultar_Agendamento
    def __str__(self):
        return self.alterar_Agendamento
    def __str__(self):
        return self.remover_Agendamento