from django.shortcuts import render, get_object_or_404
from .models import Evento, Local
# Create your views here.

def index(request):
    eventos = Evento.objects.all()
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        eventos = eventos.filter(categoria__id=categoria_id)

    return render(request, 'eventos/index.html', {'eventos': eventos})

def detalhe(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/detalhe.html', {'evento': evento})

def local(request, pk):
    local = get_object_or_404(Local, pk=pk)
    eventos = Evento.objects.all()
    contexto ={ 'local': local,
        'eventos': eventos,
    }
    return render(request, 'eventos/local.html', contexto)

