from django.contrib import admin

from .models import Comentario
from .models import Publicacion

admin.site.register(Comentario)
admin.site.register(Publicacion)