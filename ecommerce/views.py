from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Produto
from .models import Cliente


 # sobre prooduto (tela de cadastro de produtos)
def formProduto(request):
    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')
        imagem1 = request.FILES.get('imagem1')
        imagem2 = request.FILES.get('imagem2')
        imagem3 = request.FILES.get('imagem3')

        produto = Produto()
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        produto.quantidade = quantidade
        produto.imagem1 = imagem1
        produto.imagem2 = imagem2
        produto.imagem3 = imagem3
        
        produto.save()
        return redirect('lista_produtos')  # Redireciona para a lista de produtos após o salvamento

    return render(request, 'form_produto.html')

# mostrar a lista de produtos(tela inicial)
def lista_Produtos(request):
    nome_produto = request.GET.get('nome_produto')
    valor_min = request.GET.get('valor_min')
    valor_max = request.GET.get('valor_max')
    ordem = request.GET.get('ordem')

    print("Produto pesquisado: ", nome_produto)

    produtos = Produto.objects.all()

    if nome_produto:
        produtos = Produto.objects.filter(nome__icontains=nome_produto)

    if valor_min and valor_max:
        try:
            valor_min = float(valor_min)
            valor_max = float(valor_max)
            produtos = Produto.objects.filter(preco__range=(valor_min, valor_max))
        except ValueError:
            produtos = Produto.objects.all()  # Caso o filtro de valores não seja válido

    if ordem:
        if ordem == '1':
            produtos = Produto.objects.all().order_by("nome")
        elif ordem == '2':
            produtos = Produto.objects.all().order_by("preco")
        elif ordem == '3':
            produtos = Produto.objects.all().order_by("-nome")
        elif ordem == '4':
            produtos = Produto.objects.all().order_by("-preco")

    return render(request, 'lista_produtos.html', {'produtos': produtos})

# detalhes do produto (tela de detalhes do produto)
def detalhesProduto(request, id):
    print(id)
    produto = get_object_or_404(Produto, pk=id)

    imagens = []
    if produto.imagem1:
        imagens.append(produto.imagem1.url)
    if produto.imagem2:
        imagens.append(produto.imagem2.url)
    if produto.imagem3:
        imagens.append(produto.imagem3.url)

    return render(request, "detalhes_produto.html", {"produto": produto, "imagens": imagens})

# atualizar produto (tela de atualização dos dados do produto)
def atualizarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        print("DAdos recebidos com sucesso!")

        produto.nome = request.POST.get('nome', produto.nome)
        produto.descricao = request.POST.get('descricao', produto.descricao)

        preco_novo = request.POST.get('preco', None)
        if preco_novo:
            try:
                produto.preco = float(preco_novo)
            except ValueError:
                pass
        
        quantidade_nova = request.POST.get('quantidade', None)
        if quantidade_nova:
            try:
                produto.quantidade = int(quantidade_nova)
            except ValueError:
                pass
        
        for i in range(1,5):
            campo_imagem = f'imagem{i}'
            if campo_imagem in request.FILES:
                setattr(produto, campo_imagem, request.FILES[campo_imagem])

        produto.save()
    return render(request, 'atualizar_produto.html', {'produto':produto})




 # sobre clientes (tela de cadastro de clientes)
def formCliente(request):
    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')

        cliente = Cliente()
        cliente.nome = nome
        cliente.telefone = telefone
        cliente.endereco = endereco
        cliente.cidade = cidade

        cliente.save()

    return render(request, 'form_cliente.html')

# mostrar a lista de clientes 
def lista_Clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})



# acessar a página inicial ( tela Mais 'formularios')
def formulario(request):
    if request.method == 'POST':
        escolha = request.POST.get('escolha')

        if escolha == 'produto':
            return redirect('form_produto')

        elif escolha == 'cliente':
            return redirect('form_cliente')
        
        elif escolha == 'atualizar':
            return redirect('atualizar_produto')

    return render(request, 'formulario.html')




