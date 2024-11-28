from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Dangal(request):
    return HttpResponse('<h1 style="color: crimson;">Dangal is the top most Box Office Collection movie.</h1>')

def jawaan(request):
    return HttpResponse('<h1 style="color: blue;">Jawan is the one of the best movie in 2023</h1>')
