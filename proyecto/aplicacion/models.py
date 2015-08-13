from django.db import models

class libros(models.Model):
	titulo=models.CharField(blank=False,max_length=60)
	autor=models.CharField(blank=False, max_length=60)
	precio=models.DecimalField(max_digits=6, decimal_places=2)
	stock=models.IntegerField(blank=False)
	id_editorial=models.IntegerField(blank=False)