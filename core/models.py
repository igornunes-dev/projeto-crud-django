from django.db import models
from stdimage.models import StdImageField
# Create your models here.

#Signals
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
  criado = models.DateField('Data de Criação', auto_now=True)
  modificado = models.DateField('Data de Atualização', auto_now=True)
  ativo = models.BooleanField('Ativo?', default=True)

  # classe Base é abstrata (abstract = True), ou seja, não cria uma tabela no banco de dados.
  class Meta:
    abstract = True


class Produto(Base):
  nome = models.CharField('Nome', max_length=100)
  preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
  estoque = models.IntegerField('Estoque')
  imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (420, 420)})
  slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

  def __str__(self):
    return self.nome
  
def produto_pre_save(signal, instance, sender, **kwargs):
  instance.slug = slugify(instance.nome)

#Essa conexão é como um alarme: antes de salvar um Produto, ele chama a função produto_pre_save para preparar o campo slug
signals.pre_save.connect(produto_pre_save, sender=Produto)