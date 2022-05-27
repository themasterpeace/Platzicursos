from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Estas en la pagina principal de Premios Platzi App")

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta no. {question_id}")

def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta no. {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta no. {question_id}")