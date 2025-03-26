from django.shortcuts import render, redirect
from .models import Produto
from .models import Cliente

# Create your views here.

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
def index(request):
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
    return render(request, 'index.html')

#mostrar a lista de produtos
def lista_Produtos(request):
    produtos = Produto.objects.all()

    for prod in produtos:
        print("R${:,.2f}".format(prod.preco))

    return render(request, 'lista_produtos.html', {'produtos': produtos})

#mostrar a lista de clientes
def lista_Clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

