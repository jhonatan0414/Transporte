from django.shortcuts import render

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import cupo
from cliente.models import cliente
from ruta.models import ruta
from .forms import cupoForm

def inicio(request):
    Cupo = cupo.objects.all()
    Cliente = cliente.objects.all()
    Ruta = ruta.objects.all()
    return render(request, 'inicio.html', {'cupo': Cupo, 'cliente': Cliente, 'ruta': Ruta})

def cupoCreation(request, template='cupoForm.html'):
    form = cupoForm()
    if request.method == "POST":
        form = cupoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'cupoNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def cupoList(request):
    Cupo = cupo.objects.all()
    return render(request, 'cupoListado.html', {'cupo': Cupo})

def cupoDetail(request, id, template='rutaDetalle.html'):
    Cupo = get_object_or_404(cupo, pk=id)
    return render_to_response(template, {'cupo': Cupo}, context_instance=RequestContext(request))

def cupoDelete(request, id_Codigo):
    instance = get_object_or_404(cupo, id=id_Codigo)
    instance.delete()
    Cupo = cupo.objects.all()
    return render(request, 'cupoListado.html', {'cupo': Cupo})

def cupoUpdate(request, id_Codigo):
    instance = get_object_or_404(cupo, id=id_Codigo)
    form = cupoForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Cupo = cupo.objects.all()
            return render(request, 'cupoListado.html', {'cupo': Cupo})
    return render(request, 'cupoDetalle.html', {'form': form})
