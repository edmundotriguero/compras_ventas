from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    description = models.CharField(
        max_length=100, 
        help_text='Descripcion de la categoria', 
        unique=True
    )

# para devolver el primer parametro 
    def __str__(self):
        return '{}'.format(self.description)

    # guarda la decripcion en mayusculas
    def save(self):
        self.description = self.description.upper()
        super(Categoria, self).save()

    #modifica para que el prural sea corecto en el spanil
    class Meta:
        verbose_name_plural = "Categorias"


