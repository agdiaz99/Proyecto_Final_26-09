from django.urls import path
from blog.views import *

urlpatterns = [
    path('post/', post, name='post'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('<slug:slug>/', publicaciones_detalle, name='publicaciones_detalle'),
]