from django.db import models

class Product(models.Model): 
	name = models.CharField(max_length=233) 
	desc = models.TextField() 
	price = models.PositiveSmallIntegerField() 
	image = models.FileField(upload_to='product')

	def __str__(self):
		return self.name
