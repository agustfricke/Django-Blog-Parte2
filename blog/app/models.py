from django.db import models

class Publicacion(models.Model):
    titulo      = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    email       = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.titulo + ' | ' + self.descripcion