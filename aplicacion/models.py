from django.db import models

# Create your models here.
class alumnos(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"



class profesores(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=16)
    especialidad = models.CharField(max_length=16)
    email = models.EmailField()


    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.especialidad} - {self.email}"