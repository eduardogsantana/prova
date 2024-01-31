from django.db import models

class Consulta(models.Model):
    SEXO_CHOICES = (
        ('MA', 'Masculino'),
        ('FE', 'Feminino'),
        ('NI', 'Prefere não Informar')
    )

    nome_do_paciente = models.CharField(max_length=120)
    procedimento = models.CharField(max_length=120)
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES, default='NI')
    idade = models.IntegerField()
    dia = models.DateField()
    horario = models.TimeField()
    data_cad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self. nome_do_paciente