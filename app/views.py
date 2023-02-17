from django.shortcuts import render
from .models import Product
from django.utils import timezone
#Define as funções que indicam o que será feito naquela rota e envia para o urls

def home(request):
    return render(request, 'global/home.html')

def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'global/product_list.html', {'products': products})

