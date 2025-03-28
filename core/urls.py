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
from django.contrib import admin
from django.urls import path
from ecommerce  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.produtoEdit, name='produto_edit'),
    path('produto/', views.formProduto, name='form_produto'),
    path('produtos/', views.lista_Produtos, name='lista_produtos'),
    path('cliente/', views.formCliente, name='form_cliente'),
    path('clientes/', views.lista_Clientes, name='lista_clientes'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()


