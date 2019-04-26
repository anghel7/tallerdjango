from django.views import generic
from django.urls import reverse_lazy

from .models import Producto


class IndexView(generic.ListView):
    model = Producto
    context_object_name = 'lista_productos'
    template_name = 'productos/index.html'


class CreateView(generic.CreateView):
    model = Producto
    fields = ('nombre', 'descripcion', 'precio', 'cantidad')
    template_name = 'productos/create.html'
    success_url = reverse_lazy('product_list')


class UpdateView(generic.UpdateView):
    model = Producto
    fields = ('nombre', 'descripcion', 'precio', 'cantidad')
    template_name = 'productos/create.html'
    success_url = reverse_lazy('product_list')


class DeleteView(generic.DeleteView):
    model = Producto
    success_url = reverse_lazy('product_list')
    template_name = 'productos/confirm_delete.html'


class DetailView(generic.DetailView):
    model = Producto
    template_name = 'productos/detail.html'
    context_object_name = 'producto'
