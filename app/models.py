from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Arte(models.Model):
    titulo = models.CharField('Título',max_length=150, blank=False)
    autor = models.CharField('Autor',max_length=150, blank=False)
    avaliacao = models.FloatField('Avaliação',validators=[MaxValueValidator(5.0),MinValueValidator(0.0)],
                                  blank=True, null= True)

    def __str__(self):
        return f'{self.titulo} - by {self.autor}'


class Poesia(Arte):
    corpo = models.TextField(blank=False)


class Pintura(Arte):
    imagem = models.ImageField('Imagem')


