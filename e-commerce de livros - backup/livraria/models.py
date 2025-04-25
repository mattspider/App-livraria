from ast import Delete
from statistics import quantiles
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.


class Livros(models.Model):

    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    valor = models.IntegerField()
    image = models.ImageField()


    aval = models.IntegerField(default=0,null=True)
    qtd_avaliation = models.IntegerField(default=0,null=True)
    total_stars = models.IntegerField(default=0,null=True)
    media = models.IntegerField(default=0,null=True)



    class Meta:
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livros = models.ForeignKey(Livros,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Carrinho'
    def __str__(self):
        return 'carrinho de:' 


class Vote(models.Model):
    livros =models.ForeignKey(Livros, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Vote'
