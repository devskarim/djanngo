from django.urls import path 
from .views import CreateProductView, UpdateProductView, Home 

urlpatterns = [ 
	path("", Home.as_view(), name="home"), 
	path('create/', CreateProductView.as_view(), name='create'), 
	path('update/<int:pk>', UpdateProductView.as_view(), name='update')
]