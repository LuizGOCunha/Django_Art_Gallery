from django.shortcuts import render
from . import models
# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def roadnottaken(request):
    return render(request, 'roadnottaken.html')


def ozymandias(request):
    return render(request, 'ozymandias.html')


def if_p(request):
    return render(request, 'if.html')


def poesias(request):
    poesias = models.Poesia.objects.all()
    return render(request, 'poesias.html',context={'poesias': poesias})


def poesia(request):
    nome_da_poesia = models.Poesia.titulo
    autor_da_poesia = models.Poesia.autor
    corpo_da_poesia = models.Poesia.corpo
    return render(request, 'poesia.html', context={'nome':nome_da_poesia,
                                                   'autor':autor_da_poesia,
                                                   'corpo':corpo_da_poesia})