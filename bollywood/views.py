from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Dangal(request):
    return HttpResponse('<h1>Dangal is the top most Box Office Collection movie.</h1>')
