from django.urls import path
from . import views
app_name = "album_manager"

urlpatterns = [
    path("", views.index, name='index'),
    # URLs para Artista
    path('artistas/<int:pk>/', views.detalle_artista, name='detalle_artista'),
    path('artistas/crear/', views.crear_artista, name='crear_artista'),
    path('artistas/editar/<int:pk>/', views.editar_artista, name='editar_artista'),
    path('artistas/eliminar/<int:pk>/', views.eliminar_artista, name='eliminar_artista'),

    # URLs para Álbum
    path('albumes/', views.lista_albumes, name='lista_albumes'),
    path('albumes/<int:pk>/', views.detalle_album, name='detalle_album'),
    path('albumes/crear/', views.crear_album, name='crear_album'),
    path('albumes/editar/<int:pk>/', views.editar_album, name='editar_album'),
    path('albumes/eliminar/<int:pk>/', views.eliminar_album, name='eliminar_album'),
]