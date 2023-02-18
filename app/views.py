from django.shortcuts import render
#Define as funções que indicam o que será feito naquela rota e envia para o urls

def home(request):
    return render(request, 'global/home.html')

def userPage(request, id):
    return render(request, 'global/userPage.html')

def register(request):
    return render(request, 'global/register.html')

