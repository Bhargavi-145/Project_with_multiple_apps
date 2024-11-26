from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pushpa(request):
    return HttpResponse('<h1>Pushpa is the PAN india movie</h1>')
