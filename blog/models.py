from django.db import models
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=30)
	slug = models.SlugField()
	intro = models.CharField(max_length=30)
	cuerpo = models.CharField(max_length=255)
	fecha = models.DateTimeField(default=now)

	class Meta:
		ordering = ['-fecha']


class Comentario(models.Model):
	post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
	nombre = models.CharField(max_length=255)
	email = models.EmailField()
	cuerpo = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-fecha']