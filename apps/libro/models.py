from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 200, blank = False, null = False)
    apellidos = models.CharField('Apellido', max_length = 200, blank = False, null = False)
    nacionalidad = models.CharField('Nacionalidad', max_length = 200, blank = False, null = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre'] #ordena alfabeticamente por nombre

    def __str__(self):
        return self.nombre