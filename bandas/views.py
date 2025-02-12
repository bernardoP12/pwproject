from django.shortcuts import render, redirect
from .models import Banda, Album, Musica
from django.contrib.auth.decorators import login_required
from .forms import BandaForm, AlbumForm, MusicaForm

# Create your views here.

def index_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome'),
        'bandas_rock' : Banda.objects.filter(genero__contains='Rock'),
        'bandas_metal' : Banda.objects.filter(genero__contains='Metal'),
        'bandas_grunge' : Banda.objects.filter(genero__contains='Grunge')

    }
    return render(request,'bandas/index.html',context)


def banda_view(request, banda_id):
    context = {
        'banda': Banda.objects.get(id=banda_id),
        'albuns': Album.objects.filter(banda = banda_id).order_by('titulo'),
    }

    return render(request,'bandas/banda.html',context)

def album_view(request,album_id):
    context = {
        'album': Album.objects.get(id=album_id),
        'musicas': Musica.objects.filter(album = album_id).order_by('titulo')
    }

    return render(request,'bandas/album.html',context)

def musica_view(request,musica_id):
    context = {
        'musica': Musica.objects.get(id=musica_id),
    }
    return render(request,'bandas/musica.html',context)


@login_required
def nova_banda_view(request):
    form = BandaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:index')

    context = {'form': form}
    return render(request, 'bandas/novaBanda.html', context)


@login_required
def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:index')
    else:
        form = BandaForm(instance=banda)

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/editarBanda.html', context)

@login_required
def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:index')

@login_required
def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:index')
    else:
        form = AlbumForm(instance=album)

    context = {'form': form, 'album':album}
    return render(request, 'bandas/editarAlbum.html', context)


@login_required
def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas:index')


@login_required
def novo_album_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    form = AlbumForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        album = form.save(commit=False)
        album.banda = banda
        album.save()
        return redirect('bandas:album')

    context = {'form': form}
    return render(request, 'bandas/novoAlbum.html', context)

@login_required
def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:index')
    else:
        form = MusicaForm(instance=musica)

    context = {'form': form, 'musica':musica}
    return render(request, 'bandas/editarMusica.html', context)


@login_required
def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandas:index')


@login_required
def nova_musica_view(request, album_id):
    album = Album.objects.get(id=album_id)
    form = MusicaForm(request.POST or None, request.FILES)

    if form.is_valid():
        musica = form.save(commit=False)
        musica.album = album
        musica.save()
        return redirect('bandas:musica')

    context = {'form': form}
    return render(request, 'bandas/novaMusica.html', context)


