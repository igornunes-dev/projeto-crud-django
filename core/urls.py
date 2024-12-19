from django.urls import path
from .views import index, contato, produto, editarProduto

urlpatterns = [
  path('', index, name='index'),
  path('contato/', contato, name='contato'),
  path('produto/', produto, name='produto'),
  #editarProduto é a view que vai ser usada
  path('editarProduto/<int:id>/', editarProduto, name='editarProduto')
]