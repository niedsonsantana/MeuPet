from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model


# Create your models here.

class Animal(models.Model):
    usuario = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    PORTE_ESCOLHAS = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    )
    porte = models.CharField(max_length=1, choices=PORTE_ESCOLHAS)
    cor = models.CharField(max_length=8)
    castrado = models.BooleanField()
    TIPO_ESCOLHA = (
        ('CÃO', 'Cão'),
        ('GATO', 'Gato'),
    )
    tipo = models.CharField(max_length=4, choices=TIPO_ESCOLHA)
    image = StdImageField('Imagem', upload_to = './images', null = True, blank = True, variations={'thumb': {'width': 900, 'height': 650, 'crop': True}})
    info = models.TextField()
    email = models.CharField(max_length=70)
    fone = models.CharField(max_length=25)
    cidade = models.CharField(max_length=30)

    def __str__(self):
        return self.nome