from django.shortcuts import render, redirect
from .models import Produto
from .models import Cliente
from .forms import FormLogin
from .models import Administrador


def login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            administrador = Administrador.objects.filter(
                email=email, senha=senha).first()
            if administrador:
                request.session['administrador_id'] = administrador.id
                return redirect('index')
    else:
        form = FormLogin()
    return render(request, 'login.html', {'form': form})

def logout(request):
    del request.session['administrador_id']
    return redirect('login')

def index(request):
    if 'administrador_id' in request.session:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')
    

def formProduto(request):
    if request.method == 'POST':
        print("Dados recebidos com sucesso")

        nome = request.POST.get('nome')
        marca = request.POST.get('marca')
        imagem = request.FILES.get('imagem')
        preco = request.POST.get('preco')
        quantidade = request.POST.get('quantidade')

        produto = Produto()
        produto.nome = nome
        produto.marca = marca
        produto.imagem = imagem
        produto.preco = preco
        produto.quantidade = quantidade

        produto.save()

    return render(request, 'form_produto.html')


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

# Define a função index que será chamada quando o usuário acessar a página inicial


def indexMenu(request):
    # Verifica se o método de requisição é POST (envio de formulário)
    if request.method == 'POST':
        # Recupera o valor do campo "escolha" do formulário
        escolha = request.POST.get('escolha')

        # Verifica se o usuário escolheu o formulário de produtos
        if escolha == 'produto':
            # Redireciona o usuário para a página do formulário de produtos
            return redirect('form_produto')

        # Verifica se o usuário escolheu o formulário de clientes
        elif escolha == 'cliente':
            # Redireciona o usuário para a página do formulário de clientes
            return redirect('form_cliente')

    # Se o método de requisição não é POST, renderiza a página inicial
    return render(request, 'index_menu.html')

# mostrar a lista de produtos


def lista_Produtos(request):
    produtos = Produto.objects.all()

    for prod in produtos:
        print("R${:,.2f}".format(prod.preco))

    return render(request, 'lista_produtos.html', {'produtos': produtos})

# mostrar a lista de clientes


def lista_Clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})
