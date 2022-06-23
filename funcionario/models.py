from django.db import models

class Funcionario(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNascimento = models.DateField(max_length=100)
    carteiraTrabalho = models.CharField(max_length=100)
    salario = models.IntegerField(max_length=100)
    pis = models.CharField(max_length=100)

    def __str__(self):
        return self.consultar_Imoveis
    def __str__(self):
        return self.manter_Anuncio
    def __str__(self):
        return self.manter_Cliente
    def __str__(self):
        return self.manter_Funcionario
    def __str__(self):
        return self.manter_Agendamento
    def __str__(self):
        return self.gerar_Relatorio
    def __str__(self):
        return self.calcular_Salario