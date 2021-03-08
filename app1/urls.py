from django.urls import path
from .views import ListAndCreate, EditarComentario, BorrarComentario

app_name = 'app1'

urlpatterns = [

    path('', ListAndCreate.as_view() , name='prueba'),
    path('Editar/<pk>/', EditarComentario.as_view() , name='editar'),
    path('Borrar/<pk>/', BorrarComentario.as_view() , name='borrar'),
]