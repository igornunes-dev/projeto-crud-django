from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto

def index(request):
  context = {
    'produtos': Produto.objects.all()
  }

  return render(request, 'index.html', context)

def contato(request):
  #forma comum no Django de inicializar um formulário com os dados de uma requisição HTTP (como POST) ou deixar o formulário vazio caso não haja dados enviados
  form = ContatoForm(request.POST or None)

  if request.method == 'POST':
    #is_valid() -> Se o formulário não tiver erro
    if form.is_valid():
      form.sendEmail()

      messages.success(request, 'Formulário enviado com sucesso')
      #reseta o formulário 
      form = ContatoForm()
    else:
      messages.error(request, 'Erro ao enviar E-mail')

  context = {
    'form': form
  }
  return render(request, 'contato.html', context)

def produto(request):
  if request.method == 'POST':
    form = ProdutoModelForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()

      messages.success(request, 'Produto salvo com sucesso')
      form = ProdutoModelForm()
    else: 
      messages.error(request, 'Erro ao salvo Produto')
  else:
    form = ProdutoModelForm()

  context = {
    'form': form
  }
  return render(request, 'produto.html', context)

#Precisa receber o id que vem da url
def editarProduto(request, id):
    produto = Produto.objects.get(id=id)
    
    if request.method == 'POST':
        #O form é instanciado com os request.POST:dados enviados do usuario, request.FILES:os arquivos, instance=produto:informa que os dados devem ser aplicados ao objeto existente.
        form = ProdutoModelForm(request.POST, request.FILES, instance=produto)
        #Se o botão "Deletar" for clicado, o parâmetro delete estará presente no request.POST
        if 'delete' in request.POST:
           produto.delete()
           return redirect('index')
        #Se o botão "Edit" for clicado, o parâmetro delete estará presente no request.POST
        elif 'edit' in request.POST:
          if form.is_valid():
            form.save()  
            return redirect('index')
    else:
        form = ProdutoModelForm(instance=produto)

    context = {
       'form': form,
       'produto': produto
    }
    
    return render(request, 'editarProduto.html', context)
