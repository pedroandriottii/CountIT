from django.shortcuts import render
#Define as funções que indicam o que será feito naquela rota e envia para o urls

def home(request):
    return render(request, 'global/home.html')

def createUser(request):
    return render(request, 'global/signin.html')

def userPage(request):
    return render(request, 'global/userPage.html')