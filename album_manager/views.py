from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Artista, Album
from .forms import ArtistaForm, AlbumForm

def index(request):
    artistas = Artista.objects.order_by('nombre')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'artistas':artistas
    },
    request))

# Vistas para Artista
def detalle_artista(request, pk):
    artista = get_object_or_404(Artista, pk=pk)
    template = loader.get_template('detalle_artista.html')
    context = {
        'artista': artista
    }
    return HttpResponse(template.render(context,request))

def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistaForm()
    return render(request, 'crear_artista.html', {'form': form})

def editar_artista(request, pk):
    artista = Artista.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'editar_artista.html', {'form': form})

def eliminar_artista(request, pk):
    artista = Artista.objects.get(pk=pk)
    artista.delete()
    return redirect('album_manager:index')


# Vistas para Álbum
def lista_albumes(request):
    albumes = Album.objects.order_by('titulo')
    template = loader.get_template('lista_albumes.html')
    return  HttpResponse(template.render({
        'albumes': albumes
        },
        request
        ) )

def detalle_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    template = loader.get_template('detalle_album.html')
    context = {
        'album': album}
    
    return HttpResponse(template.render(context, request))

def crear_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    return render(request, 'crear_album.html', {'form': form})

def editar_album(request, album_id):
    album = Album.objects.get(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'editar_album.html', {'form': form})

def eliminar_album(request, pk):
    album = Album.objects.get(pk=pk)
    album.delete()
    return redirect('album_manager:index')

