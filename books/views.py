from django.shortcuts import render, HttpResponse
from .models import Books

def index(request):
    books = Books.objects.all()
    return render(request, 'pages/index.html', {'books': books})

def search(request):
    q = request.GET.get('search')
    contatos = Books.objects.filter(nome__icontains=q) # o __icontains é para filtrar o que tem com o que foi digitado, sem isso, ele pesquisa por algo que seja igual
    return render(request, 'pages/index.html', {'contatos': contatos})
