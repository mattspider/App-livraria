from django.db import models


class Livros(models.Model):    


    titulo = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    autor = models.CharField(max_length=255, null=True, blank=True)
    valor = models.IntegerField(null=True, default=0)
    aval = models.IntegerField(null=True, default=0)
    qtd_avaliation = models.IntegerField(null=True, default=0)
    total_stars = models.IntegerField(null=True, default=0)
    media = models.IntegerField(null=True, default=0)
    img = models.ImageField()


    def __str__(self):
        return f"{self.titulo} {self.descricao} {self.autor} {self.valor} {self.aval} {self.qtd_avaliation} {self.total_stars} {self.media}"

    class Meta:
        verbose_name_plural = "Livro"

