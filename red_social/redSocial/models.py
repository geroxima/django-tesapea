from django.db import models

class Publicacion(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    publicacion = models.ForeignKey(Publicacion,
    on_delete=models.CASCADE, related_name='comentarios')