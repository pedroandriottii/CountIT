from django.urls import path
from . import views
# Informa o caminho da url, subdominio e a função que irá ser executada quando for feito a requisição da rota

urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login, name="login"),

]
