from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def avengers(request):
    return HttpResponse('<h1 style="color: red;">Avengers is the second-highest-grossing Hollywood film worldwide</h1>')

def titanic(request):
    return HttpResponse('<h1 style="color: crimson;">The main themes this film include love, class conflict, and tragedy</h1>')
