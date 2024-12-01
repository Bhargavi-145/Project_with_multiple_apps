from django.urls import path
from bollywood.views import *

urlpatterns = [
    path('Dangal/', Dangal, name='Dangal'),
    path('jawaan/', jawaan, name='jawaan'),
]
