from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion, Comentario
from .forms import PublicacionForm, ComentarioForm

def publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha')
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})


def nueva_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.save()
            return redirect('publicaciones')
    else:
        form = PublicacionForm()
        return render(request, 'nueva_publicacion.html', {'form': form})


#Entrar en una publicacion especifica y poder dejar comentarios
def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = publicacion.comentarios.all()
    nuevo_comentario = None
    if request.method == 'POST':
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            nuevo_comentario = form_comentario.save(commit=False)
            nuevo_comentario.autor = request.user
            nuevo_comentario.publicacion = publicacion
            nuevo_comentario.save()
            return redirect('publicacion_detalle', pk=pk)
    else:
        form_comentario = ComentarioForm()
        return render(request, 'publicacion_detalle.html', {'publicacion':
        publicacion, 'comentarios': comentarios, 'form_comentario':
        form_comentario})