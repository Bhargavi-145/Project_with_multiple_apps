from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pushpa(request):
    return HttpResponse('<h1>Pushpa is the PAN india movie</h1>')

def amaran(request):
    return HttpResponse('<h1 style="color: green;">Amaran is based on the true story of Major Mukund Varadarajan</h1>')

def three(request):
    return HttpResponse('<h1 style="color: hotpink;">One of my favorite movie</h1>')
