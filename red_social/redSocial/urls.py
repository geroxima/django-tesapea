from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicaciones, name='publicaciones'),
    path('publicacion/<int:pk>', views.publicacion_detalle, name='publicacion_detalle'),
    path('nueva_publicacion/', views.nueva_publicacion, name='nueva_publicacion'), 

]