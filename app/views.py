from django.shortcuts import render, HttpResponse
from .models import Product
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
#Define as funções que indicam o que será feito naquela rota e envia para o urls

def home(request):
    return render(request, 'global/home.html')

def product_list(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'global/product_list.html', {'products': products})
    else:
        return HttpResponse('Você precisa estar logado!')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'global/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Usuário Já Cadastrado!')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('Usuário Cadastrado com Sucesso!')

        

def login(request):
    if request.method == "GET":
        return render(request, 'global/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login_django(request, user)
            return HttpResponse('Login Realizado com Sucesso!')
        else:
            return HttpResponse('E-mail ou Senha Inválidos!')
