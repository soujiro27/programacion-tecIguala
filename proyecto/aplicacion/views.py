from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.db import models

def pinta(request):
	lista=['inicio','contacto','nosotros']
	ahora=datetime.now()
	# plantilla=get_template("hora.html")
	# contenido=Context({"tiempo":ahora, "lista":lista})
	# html=plantilla.render(contenido)

	



def home(request):
	return HttpResponse("pantalla de django")

def saludo(request):
	x=5
	y=20
	total=x+y
	return HttpResponse("la suma es %i" % total)



def peticion(request):
	return HttpResponse("el response tiene %s" % request)