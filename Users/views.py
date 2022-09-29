from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from blog.models import Post
from Users.forms import UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Imports para login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


@login_required(login_url=reverse_lazy("login"))
def inicio(request):
    return render(request, "Users/inicio.html")

def nosotros(request):
    return render(request, "Users/nosotros.html")


@login_required(login_url=reverse_lazy("login"))
def perfil(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
	else:
		user = current_user
	return render(request, "Users/perfil.html", {"user":user})


@login_required(login_url=reverse_lazy("login"))
def buscar(request):
    return render(request, "Users/buscar.html")


@login_required(login_url=reverse_lazy("login"))
def buscar_blog(request):
    if request.GET["titulo"]:
        name=request.GET["titulo"]
        posts=Post.objects.filter(nombre=name)
        if len(posts)!=0:
            return render(request, "Users/resultado_busqueda.html", {"posts":posts})
        else:
            return render(request, "Users/resultado_busqueda.html", {"mensaje": "No hay resultados con ese nombre"})
    else:
        return render(request, "Users/buscar.html", {"mensaje": "Por favor, ingrese una búsqueda"})


############# (Login), (Register), (Logout), (Editar perfil), (Agregar avatar) y (Obtener avatar) #############


def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            #Podríamos fijarnos que no exista un user en la bd. con ese nombre
            form.save()
            return render(request, 'Users/inicio.html', {'mensaje':f"¡Usuario @{username} creado con éxito!"})
    else:
        form=UserRegisterForm()
    return render(request, 'Users/register.html', {'form':form})


def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'Users/inicio.html', {"mensaje":f"¡Hola de nuevo!"})
            else:
                return render(request, 'Users/login.html', {"form":form, "mensaje":'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'Users/login.html', {"form":form, "mensaje":'Usuario o contraseña incorrectos'})
    else:
        form=AuthenticationForm()
        return render(request, 'Users/login.html', {"form":form})


@login_required(login_url=reverse_lazy("login"))
def editar_perfil(request):
    usuario=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.username=form.cleaned_data["username"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password2"]
            usuario.save()
            return render(request, 'Users/inicio.html', {"mensaje":f"¡Perfil editado exitosamente!"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'Users/editar_perfil.html', {"form":form, "usuario":usuario})


@login_required(login_url=reverse_lazy("login"))
def añadir_avatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data["imagen"])
            avatar.save()
            return render(request, 'Users/inicio.html', {"usuario":request.user, "mensaje":"¡Avatar agregado exitosamente!"})
    else:
        formulario=AvatarForm()
    return render(request, 'Users/añadir_avatar.html', {"form":formulario, "usuario":request.user})


# Función que trae la URL del avatar
@login_required(login_url=reverse_lazy("login"))
def obtener_avatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="Users/static/Users/perfil-default.png"
    return imagen