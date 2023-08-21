from django.db import models

# Create your models here.

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    Imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    Nombre= models.CharField(max_length=100,default=' ', verbose_name='Nombre')
    Apellido= models.CharField(max_length=100,default=' ',verbose_name='Apellido')
    Correo= models.CharField(max_length=100,default=' ',verbose_name='Correo')
    HistorialConsultas= models.TextField(verbose_name='Descripcion Cotizacion',null=True)


def __str__(self):
    fila = "Nombre: " + self.Nombre + " - " + "Cotizaciones: " + self.HistorialConsultas
    return fila

def delete(self,using=None,keep_parents=False):
    self.Imagen.storage.delete(self.Imagen.name)
    super().delete()
