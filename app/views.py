from django.shortcuts import render
from app.forms import PersonForm

def paginainicial(request):
    return render(request, 'paginaInicial.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    data = {}
    data['form'] = PersonForm()
    return render(request, 'cadastro.html', data)

def upload(request):
    return render(request, 'upload.html')

def download(request):
    return render(request, 'download.html')
