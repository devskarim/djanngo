from django.urls import path 
from .views import CreateProductView, UpdateProductView, Home, DetailProducView,DeleteProductView

urlpatterns = [ 
	path("", Home.as_view(), name="home"),
	path('create/', CreateProductView.as_view(), name='create'), 
	path('detail/<int:pk>', DetailProducView.as_view(), name='detail'),
	path('update/<int:pk>', UpdateProductView.as_view(), name='update'),
	path('delete/<int:pk>', DeleteProductView.as_view(), name='delete')
]