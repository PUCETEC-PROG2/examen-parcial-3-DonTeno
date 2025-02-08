from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=80)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    año_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)

    def __str__(self):
        return self.titulo