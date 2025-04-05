"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from ecommerce import views

urlpatterns = [
    # produto
    path('', views.lista_Produtos, name='lista_produtos'),
    path('formulario', views.formulario, name='formulario'),
    path('produto/cadastro', views.cadastroProduto, name='cadastro_produto'),
    path('produto/<int:id>', views.detalhesProduto, name='detalhes_produto'),
    path('produto/atualizar/', views.atualizarProduto, name='atualizar_produto'),
    path('produto/adm/', views.admEstoque, name='adm_estoque'),
    path('produto/deletar/<int:id>/', views.deletarProduto, name='deletar_produto'),

    #pagamento
    path('pagamento', views.formularioPagamento, name='formulario_pagamento'),

    # cliente
    path('cliente/cadastro', views.cadastroCliente, name='cadastro_cliente'),
    path('cliente/', views.formCliente, name='form_cliente'),
    path('clientes/', views.lista_Clientes, name='lista_clientes'),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()
