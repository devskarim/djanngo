from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.urls import reverse_lazy

from .models import Product

class Home(TemplateView):
	model = Product
	template_name = 'index.html'


class  CreateProductView(CreateView): 
	model = Product
	template_name = 'create.html'
	fields = ['name', 'desc', 'price', 'image']
	success_url = reverse_lazy('home')


class UpdateProductView(UpdateView):
	model = Product 
	template_name = "update.html" 
	fields = ['name', 'desc', 'price', 'image'] 
	success_url = reverse_lazy('home')
