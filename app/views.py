from django.shortcuts import render


def paginainicial(request):
    return render(request, 'paginaInicial.html')


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def upload(request):
    return render(request, 'upload.html')


def download(request):
    return render(request, 'download.html')
