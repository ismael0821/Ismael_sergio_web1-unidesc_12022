from django.db import models

class Pagamento(models.Model):

    valor_pag = models.IntegerField(max_length=100)
    forma_pag = models.CharField(max_length=100)
    parcela_pag = models.IntegerField(max_length=100)
    data_Pag = models.DateField(max_length=100)
    banco_pag = models.CharField(max_length=100)
    agencia_pag = models.CharField(max_length=100)
    conta_pag = models.CharField(max_length=100)

    def __str__(self):
        return self.Pagamento