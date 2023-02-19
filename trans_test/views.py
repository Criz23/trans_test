from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
	return render(request, 'bienvenida.html')

def despedida(request):
	despedida = "Good By"
	return HttpResponse(despedida)