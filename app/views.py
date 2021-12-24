from django.shortcuts import render, get_object_or_404
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


def poesia(request, poesia_id):
    poesia = get_object_or_404(models.Poesia, pk=poesia_id)
    return render(request, 'poesia.html', context={'poesia': poesia})

def pinturas(request):
    pinturas = models.Pintura.objects.all()
    return render(request, 'pinturas.html', context={'pinturas':pinturas})


# Isso ainda é mágica pra mim...
# De onde ele tá tirando esse segundo argumento, o id da pintura? E como ele liga isso ao objeto?
# Será que a sintaxe usada no urls.py importa? (Creio que está sendo sinalizado de lá)
# Será que ele recebe esse argumento da url? (Acho que sim, pois é o sinal recebido do urls.py, é a mesma sintaxe)
def pintura(request, pintura_id):
    pintura = get_object_or_404(models.Pintura, pk=pintura_id)
    return render(request, 'pintura.html', context={'pintura':pintura})