from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def avengers(request):
    return HttpResponse('<h1>Avengers is the second-highest-grossing Hollywood film worldwide</h1>')
