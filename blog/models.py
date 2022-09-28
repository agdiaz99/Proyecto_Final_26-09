from django.db import models

# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=255)
	slug = models.SlugField()
	intro = models.TextField()
	cuerpo = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)

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