from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm, ComentarioForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy

#Imports para login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=reverse_lazy("login"))
def publicaciones(request):
    posts = Post.objects.all()
    return render(request, 'Users/publicaciones.html', {'posts': posts})


@login_required(login_url=reverse_lazy("login"))
def publicaciones_detalle(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method=="POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("publicaciones_detalle", slug=post.slug)
    else:
        form = ComentarioForm()
    return render(request, "Users/publicaciones_detalle.html", {"post":post, "form":form})


@login_required(login_url=reverse_lazy("login"))
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect("publicaciones")
	else:
		form = PostForm()
	return render(request, "Users/post.html", {"form":form })