from django.urls import path
from hollywood.views import *

urlpatterns = [
    path('avengers/', avengers, name='avengers'),
    path('titanic/', titanic, name='titanic'),
]