from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto
class ContatoForm(forms.Form):
  nome = forms.CharField(label='Nome', max_length=100)
  email = forms.EmailField(label='Email', max_length=100)
  assunto = forms.CharField(label='Assunto', max_length=120)
  mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)
  
  def sendEmail(self):
    nome = self.cleaned_data['nome']
    email = self.cleaned_data['email']
    assunto = self.cleaned_data['assunto']
    mensagem = self.cleaned_data['mensagem']

    conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

    mail = EmailMessage (
      #Assunto
      subject='Email enviado pelo sistema',
      #Conteudo
      body=conteudo,
      #Qual email esta enviando
      from_email='contato@seudominio.com.br',
      #Para
      to=['contato@seudominio.com.br'],
      #Pra qual vai ser enviado
      headers={'Reply-To': email}
    )

    mail.send()


class ProdutoModelForm(forms.ModelForm):
  class Meta: 
    model = Produto
    fields = ['nome', 'preco', 'estoque', 'imagem']