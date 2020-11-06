from django.db import models

# Create your models here.
class Departamentos(models.Model):
    name=models.CharField('nombre',max_length=100)
    short_name=models.CharField('nombre_corto',max_length=50)
    anulate=models.BooleanField('anulado', default=False)

    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.short_name
