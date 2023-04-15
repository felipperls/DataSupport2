from django.urls import path
from . import views

urlpatterns = [
    path("", views.paginainicial, name='inicio'),
    path("cadastro", views.cadastro, name='cadastro'),
    path("login", views.login, name='login'),
    path("download", views.download, name='download'),
    path("upload", views.upload, name='upload'),

]

