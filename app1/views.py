from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Comentario
from .forms import ComentarioForm
from django.urls import reverse_lazy

# Create your views here.

#FORMULARIO EN UNA MISMA PAGINA   
class ListAndCreate(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "app1/prueba.html"
    success_url = reverse_lazy('app1:prueba')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = self.model.objects.all()
        return context


class EditarComentario(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "app1/confirmar_editar.html"
    success_url = reverse_lazy('app1:prueba')


class BorrarComentario(DeleteView):
    model = Comentario
    template_name = "app1/confirmar_borrar.html"
    success_url = reverse_lazy('app1:prueba')