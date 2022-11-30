
from django.db import models

# Create your models here.
class Cidade(models.Model):
  nome = models.CharField("Nome", max_length=100)
  def __str__(self):
    return self.nome
  class Meta:
      verbose_name = "Cidade"
      verbose_name_plural = "Cidades"    


class Comentarios(models.Model):
     texto = models.CharField("Texto", max_length=255)
     nome = models.CharField("Nome", max_length=100)


class Tag(models.Model):
     nome = models.CharField("Nome", max_length=100)


class Video(models.Model):
     titulo = models.CharField("Título", max_length=100)
     descricao = models.CharField("Descricao", max_length=100, null=True)
     data = models.DateTimeField("Data")
     youtubeid = models.CharField("Youtube id", max_length=255)  
     thumb = models.CharField("Thumb", max_length=255)
     canal = models.ForeignKey('Canal', on_delete=models.PROTECT, verbose_name="Canal",null=True)
     comentarios = models.ForeignKey('Comentarios', on_delete=models.PROTECT,verbose_name="Comentarios",null=True)
     tag = models.ManyToManyField("Tag", verbose_name="Tags")


class Canal(models.Model):
     nome = models.CharField("Nome", max_length=100)
    