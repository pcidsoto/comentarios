from django.db import models

# Create your models here.
class Comentario(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField(auto_now=True)
    email = models.EmailField(max_length=50)
    texto = models.TextField(max_length=500)

    class Meta:
        ordering = ['fecha']