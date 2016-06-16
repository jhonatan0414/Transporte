from django.shortcuts import render

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import ruta
from cliente.models import cliente
from cupo.models import cupo
from .forms import rutaForm

def inicio(request):
    Ruta = ruta.objects.all()
    Cliente = cliente.objects.all()
    Cupo = cupo.objects.all()
    return render(request, 'inicio.html', {'ruta': Ruta, 'cliente': Cliente, 'cupo': Cupo})

def rutaCreation(request, template='rutaForm.html'):
    form = rutaForm()
    if request.method == "POST":
        form = rutaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'rutaNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def rutaList(request):
    Ruta = ruta.objects.all()
    return render(request, 'rutaListado.html', {'ruta': Ruta})

def rutaDetail(request, id, template='rutaDetalle.html'):
    Ruta = get_object_or_404(ruta, pk=id)
    return render_to_response(template, {'ruta': Ruta}, context_instance=RequestContext(request))

def rutaDelete(request, id_CodigoRuta):
    instance = get_object_or_404(ruta, id=id_CodigoRuta)
    instance.delete()
    Ruta = ruta.objects.all()
    return render(request, 'rutaListado.html', {'ruta': Ruta})

def rutaUpdate(request, id_CodigoRuta):
    instance = get_object_or_404(ruta, id=id_CodigoRuta)
    form = rutaForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Ruta = ruta.objects.all()
            return render(request, 'rutaListado.html', {'ruta': Ruta})
    return render(request, 'rutaDetalle.html', {'form': form})
