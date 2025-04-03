from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto
from .models import Cliente


 # sobre prooduto (tela de cadastro de produtos)
def cadastroProduto(request):
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
    
    return render(request, 'cadastro_produto.html')


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

def atualizarProduto(request):
    produto = None  # Inicializa a variável para evitar erro caso o ID não seja encontrado
    
    if request.method == "GET":
        produto_id = request.GET.get("id_produto")
        if produto_id:
            produto = Produto.objects.filter(id=produto_id).first()

    if request.method == "POST":
        produto_id = request.POST.get("id_produto")

        if not produto_id:  
            return HttpResponse("Erro: ID do produto não encontrado.", status=400)

        try:
            produto = Produto.objects.get(id=produto_id)
        except Produto.DoesNotExist:
            return HttpResponse("Erro: Produto não encontrado.", status=404)

        produto.nome = request.POST.get("nome") or produto.nome
        produto.descricao = request.POST.get("descricao") or produto.descricao

        preco = request.POST.get("preco")
        if preco:
            try:
                produto.preco = float(preco)
            except ValueError:
                return HttpResponse("Erro: O preço deve ser um número válido.", status=400)

        quantidade = request.POST.get("quantidade")
        if quantidade:
            try:
                produto.quantidade = int(quantidade)
            except ValueError:
                return HttpResponse("Erro: A quantidade deve ser um número inteiro.", status=400)

        if 'imagem1' in request.FILES:
            produto.imagem1 = request.FILES['imagem1']
        if 'imagem2' in request.FILES:
            produto.imagem2 = request.FILES['imagem2']
        if 'imagem3' in request.FILES:
            produto.imagem3 = request.FILES['imagem3']

        produto.save()

        return redirect('lista_produtos')

    return render(request, "atualizar_produto.html", {"produto": produto})

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

 # sobre cadastrar os clientes (tela de cadastro de clientes)
def cadastroCliente(request):
    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        numero_casa = request.POST.get('numero_casa')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        cliente = Cliente()
        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        cliente.cpf = cpf
        cliente.numero_casa = numero_casa
        cliente.cep = cep
        cliente.rua = rua
        cliente.cidade = cidade
        cliente.estado = estado

        cliente.save()

    return render(request, 'cadastro_cliente.html')

# mostrar a lista de clientes 
def lista_Clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})



# acessar a página inicial ( tela Mais 'formularios')
def formulario(request):
    if request.method == 'POST':
        escolha = request.POST.get('escolha')
        if escolha == 'produto':
            return redirect('cadastro_produto')
        elif escolha == 'cliente':
            return redirect('cadastro_cliente')
        elif escolha == 'atualizar':
            return redirect('atualizar_produto')
    return render(request, 'formulario.html')




