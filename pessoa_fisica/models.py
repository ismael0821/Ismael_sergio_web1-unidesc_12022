from django.db import models

class Pessoa_fisica(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNascimento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome