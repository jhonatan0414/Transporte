from django.shortcuts import render

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import cliente
from ruta.models import ruta
from cupo.models import cupo
from .forms import clienteForm

def inicio(request):
    Cliente = cliente.objects.all()
    Ruta = ruta.objects.all()
    Cupo = cupo.objects.all()
    return render(request, 'inicio.html', {'cliente': Cliente, 'ruta': Ruta, 'cupo': Cupo})

def clienteCreation(request, template='clienteForm.html'):
    form = clienteForm()
    if request.method == "POST":
        form = clienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'clienteNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def clienteList(request):
    Cliente = cliente.objects.all()
    return render(request, 'clienteListado.html', {'cliente': Cliente})

def clienteDetail(request, id, template='clienteDetalle.html'):
    Cliente = get_object_or_404(cliente, pk=id)
    return render_to_response(template, {'cliente': Cliente}, context_instance=RequestContext(request))

def clienteDelete(request, id_Cedula):
    instance = get_object_or_404(cliente, id=id_Cedula)
    instance.delete()
    Cliente = cliente.objects.all()
    return render(request, 'clienteListado.html', {'cliente': Cliente})

def clienteUpdate(request, id_Cedula):
    instance = get_object_or_404(cliente, id=id_Cedula)
    form = clienteForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Cliente = cliente.objects.all()
            return render(request, 'clienteListado.html', {'cliente': Cliente})
    return render(request, 'clienteDetalle.html', {'form': form})
