from django import forms
from .models import Artista, Album

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'pais_origen']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'año_lanzamiento', 'genero', 'artista', 'portada']