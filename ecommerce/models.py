# Create your models here.
from django.db import models  

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)   #blank=True, null=True
    quantidade = models.IntegerField()
    
    imagem1 = models.ImageField(upload_to='static/img/produto/', null=True, blank=True)
    imagem2 = models.ImageField(upload_to='static/img/produto/', null=True, blank=True)
    imagem3 = models.ImageField(upload_to='static/img/produto/', null=True, blank=True)



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)



    