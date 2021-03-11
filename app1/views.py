from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Comentario
from .forms import ComentarioForm
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect,HttpResponse,JsonResponse

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

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST,instance = self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('app1:prueba')


class BorrarComentario(DeleteView):
    model = Comentario
    template_name = "app1/confirmar_borrar.html"
    success_url = reverse_lazy('app1:prueba')