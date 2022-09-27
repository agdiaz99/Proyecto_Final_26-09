from django.urls import path
from Users.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name="nosotros"),
    path('perfil/', perfil, name='perfil'),
    path('perfil/<str:username>/', perfil, name='perfil'),

    path('buscar/', buscar, name="buscar"),
    path('buscar_usuario/', buscar_usuario, name="buscar_usuario"),

    path('register/', register, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('añadir_avatar/', añadir_avatar, name='añadir_avatar'),
]