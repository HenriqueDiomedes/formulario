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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from ecommerce import views

urlpatterns = [
    # produto
    path('', views.lista_Produtos, name='lista_produtos'),
    path('produto/cadastro', views.cadastroProduto, name='cadastro_produto'),
    path('produto/<int:id>', views.detalhesProduto, name='detalhes_produto'),
    path('produto/atualizar/', views.atualizarProduto, name='atualizar_produto'),
    path('produto/adm/', views.admEstoque, name='adm_estoque'),
    path('produto/deletar/<int:id>/', views.deletarProduto, name='deletar_produto'),

    #pagamento
    path('pagamento', views.formularioPagamento, name='formulario_pagamento'),
    path('carrinho', views.Carrinho, name='carrinho'),

    # loin
    path('cadastro', views.cadastroCliente, name='cadastro_cliente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # pos login
    path('perfil', views.perfilCliente, name='perfilcliente'),


    #login e autenticação
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(next_page='lista_produtos'), name='logout'),
    path('formulario', views.formulario, name='formulario'),

    #reset de seha e login
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),




]

urlpatterns += staticfiles_urlpatterns()
