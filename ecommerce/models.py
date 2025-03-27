# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Administrador(AbstractUser):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    imagem = models.ImageField(upload_to='static/img/produto/', null=True, blank=True)
    marca = models.CharField(max_length=255, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)   #blank=True, null=True
    quantidade = models.IntegerField()



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)