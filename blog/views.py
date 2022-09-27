from django.shortcuts import render, redirect
from .models import *
from .forms import CommentForm
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
    
    if request.method=='POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('publicaciones_detalle', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'Users/publicaciones_detalle.html.', {'post': post, 'form': form})