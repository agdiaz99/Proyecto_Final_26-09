from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='perfil-default.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)