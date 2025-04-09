from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from decimal import Decimal, InvalidOperation
from django.http import HttpResponse
from .models import Produto
from .models import Cliente, Endereco

#função para permisão de administrador
def verificar_grupo(usuario):
    return usuario.groups.filter(name='funcionario').exists()


#Funções sobre produtos:


#função para cadastrar produtos
@user_passes_test(verificar_grupo)
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










 # sobre prooduto (tela de cadastro de produtos)

# função que mostra a lista dos produtos(tela inicial)
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

#função que mostra os detalhes do produto
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

#fução que mostra o estoque de produtos(com osções de cadastrar/atualizar/deletar)
@user_passes_test(verificar_grupo)
def admEstoque(request):
    produtos = Produto.objects.all()
    return render(request, 'adm_estoque.html', {'produtos': produtos})

#função para deletar algum produto
def deletarProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()

    return redirect('adm_estoque')

# função para atualizar um produto selecionado
@user_passes_test(verificar_grupo)
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

        # Atualiza os campos básicos
        produto.nome = request.POST.get("nome") or produto.nome
        produto.descricao = request.POST.get("descricao") or produto.descricao

        # Atualiza o preço, tratando vírgula como separador decimal
        preco = request.POST.get("preco")
        if preco:
            try:
                preco = preco.replace(',', '.')
                produto.preco = Decimal(preco)
            except InvalidOperation:
                return HttpResponse("Erro: O preço deve ser um número válido.", status=400)

        # Atualiza a quantidade
        quantidade = request.POST.get("quantidade")
        if quantidade:
            try:
                produto.quantidade = int(quantidade)
            except ValueError:
                return HttpResponse("Erro: A quantidade deve ser um número inteiro.", status=400)

        # Atualiza as imagens se forem enviadas
        if 'imagem1' in request.FILES:
            produto.imagem1 = request.FILES['imagem1']
        if 'imagem2' in request.FILES:
            produto.imagem2 = request.FILES['imagem2']
        if 'imagem3' in request.FILES:
            produto.imagem3 = request.FILES['imagem3']

        produto.save()
        return redirect('adm_estoque')

    return render(request, "atualizar_produto.html", {"produto": produto})

 # sobre clientes (tela de cadastro de clientes)



#funções sobre clientes

#função para cadastrar clientes
def cadastroCliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        dataNascimento = request.POST.get('dataNascimento')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        numeroCasa = request.POST.get('numeroCasa')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')

        # Criar usuário (User do Django)
        usuario = User.objects.create_user(username=email, email=email, password=senha)
        usuario.first_name = nome
        usuario.last_name = sobrenome
        usuario.save()

        # Criar cliente
        Cliente.objects.create(
            idUsuario=usuario,
            cpf=cpf,
            dataNascimento=dataNascimento
        )

        # Criar endereço
        Endereco.objects.create(
            idUsuario=usuario,
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            telefone=telefone,          
            numero_casa=numeroCasa,
            cep=cep,
            rua=rua,
            cidade=cidade,
            estado=estado
        )

        return redirect('login')

    return render(request, 'cadastro_cliente.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('perfilCliente')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def perfilCliente(request):
    if not request.user.is_authenticated:
        return redirect('login')


    cliente = Cliente.objects.get(idUsuario=request.user)
    endereco = Endereco.objects.filter(idUsuario=request.user).first()

    return render(request, 'perfilCliente.html', {'cliente': cliente,'endereco': endereco
})

#mostrar os clientes cadastrados 'repetida'
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

# fção para mostrar a lista de clientes 
def lista_Clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})


# acessar a página inicial ( tela Mais 'formularios')
@user_passes_test(verificar_grupo)
def formulario(request):
    if request.method == 'POST':
        escolha = request.POST.get('escolha')
        if escolha == 'produto':
            return redirect('cadastro_produto')
        elif escolha == 'cliente':
            return redirect('cadastro_cliente')
        elif escolha == 'atualizar':
            return redirect('atualizar_produto')
        elif escolha == 'perfil':
            return redirect('perfilcliente')
        elif escolha == 'estoque':
            return redirect('adm_estoque')
        
    return render(request, 'formulario.html')

#funções sobre vendas


# formulario de pagamento
@user_passes_test(verificar_grupo)
def formularioPagamento(request):
    
    return render(request, 'formulario_pagamento.html')

#formulario para adicionar produto ao carrinho
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)]['quantidade'] += 1
    else:
        carrinho[str(produto_id)] = {
            'nome': produto.nome,
            'preco': float(produto.preco),
            'quantidade': 1,
            'imagem': produto.imagem1.url if produto.imagem1 else '/static/img/sem-imagem1.png',
        }

    request.session['carrinho'] = carrinho
    return redirect('exibir_carrinho')

#formulario para remover produto do carrinho
def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    if str(produto_id) in carrinho:
        del carrinho[str(produto_id)]
        request.session['carrinho'] = carrinho
    return redirect('exibir_carrinho')

#formulario para exibir produto no carrinho
def exibir_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    produtos = []
    total_geral = 0

    for produto_id, item in carrinho.items():
        try:
            produto = Produto.objects.get(id=produto_id)
            quantidade = item['quantidade']
            subtotal = produto.preco * quantidade
            total_geral += subtotal
            produtos.append({
                'id': produto.id,
                'nome': produto.nome,
                'preco': produto.preco,
                'imagem1': produto.imagem1.url if produto.imagem1 else '',
                'quantidade': quantidade,
                'subtotal': subtotal,
            })
        except Produto.DoesNotExist:
            pass  # Produto foi deletado, ignora

    return render(request, 'carrinho.html', {
        'produtos': produtos,
        'total_geral': total_geral
    })



#aumentar quantidade de produtos no carrinho
def aumentar_quantidade(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    if str(produto_id) in carrinho:
        carrinho[str(produto_id)]['quantidade'] += 1
    request.session['carrinho'] = carrinho
    return redirect('exibir_carrinho')


#diminr quantidade de produtos no carrinho
def diminuir_quantidade(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    if str(produto_id) in carrinho:
        if carrinho[str(produto_id)]['quantidade'] > 1:
            carrinho[str(produto_id)]['quantidade'] -= 1
        else:
            del carrinho[str(produto_id)]
    request.session['carrinho'] = carrinho
    return redirect('exibir_carrinho')












# função para a tela de login
def login(request):   
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

    return render(request, 'registration/login.html')
 



