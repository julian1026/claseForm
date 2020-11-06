from django.db import models
#importanto llave foranea
from aplications.departamentos.models import Departamentos

# Create your models here.
class Empleado(models.Model):
    JOB_CHOISES={
        ('0','CONTADOR'),
        ('1','INGENIERO'),
        ('2','ECONOMISTA'),
        ('3','ADMINISTRADOR'),
        ('4','OTRO'),
    }

    firs_name=models.CharField('nombres', max_length=50)
    last_name=models.CharField('apellidos', max_length=50)
    job = models.CharField('trabajo', max_length=1, choices=JOB_CHOISES)
    Departamentos=models.ForeignKey(Departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)+'-'+self.firs_name+'-'+self.last_name+'-'+self.job
