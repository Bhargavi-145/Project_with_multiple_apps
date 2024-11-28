from django.urls import path
from tollywood.views import *

urlpatterns = [
    path('pushpa/',pushpa, name='pushpa'),
    path('amaran/', amaran, name='amaran'),
]