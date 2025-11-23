from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Product

class Home(ListView):
	model = Product
	template_name = 'index.html'
	context_object_name = 'products'

class CreateProductView(CreateView): 
	model = Product
	template_name = 'create.html'
	context_object_name = 'product'
	fields = ['name', 'desc', 'price', 'image']
	success_url = reverse_lazy('home')


class UpdateProductView(UpdateView):
	model = Product 
	template_name = "update.html"
	context_object_name = 'product'
	fields = ['name', 'desc', 'price', 'image'] 
	success_url = reverse_lazy('home')


class DetailProducView(DetailView): 
	model = Product 
	template_name = 'detail.html'
	context_object_name = 'product'


class DeleteProductView(DeleteView): 
	model = Product
	template_name = 'delete.html' 
	context_object_name = 'product'
	success_url = reverse_lazy('home')