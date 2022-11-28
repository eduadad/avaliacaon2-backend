from django.db import models

# Create your models here.
class Cidade(models.Model):
  nome = models.CharField("Nome", max_length=100)
  def __str__(self):
    return self.nome
  class Meta:
      verbose_name = "Cidade"
      verbose_name_plural = "Cidades"    

