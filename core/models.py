from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    date_evento = models.DateTimeField(verbose_name="Data do Evento")
    date = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = "Evento"

