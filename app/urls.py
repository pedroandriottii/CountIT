from django.urls import path
from . import views
# Informa o caminho da url, subdominio e a função que irá ser executada quando for feito a requisição da rota

urlpatterns = [
    path('', views.home),
    path('user/<int:id>/', views.userPage)

]
