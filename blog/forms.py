from django import forms
from .models import *
from django.utils.timezone import now

class PostForm(forms.ModelForm):
	titulo = forms.CharField(label='Título', widget=forms.TextInput(attrs={'rows':1, 'placeholder': 'Ingrese un título'}), required=True)
	slug = forms.SlugField(label='Número de posteo', widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'Por ejemplo ingrese 1 si es su primer post'}), required=True)
	intro = forms.CharField(label='Introduccíon', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'Ingrese una breve introducción'}), required=True)
	cuerpo = forms.CharField(label='Contenido', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'Cuerpo'}), required=True)
	fecha = forms.DateTimeField(label='Fecha de publicación', widget=forms.DateInput(attrs={'rows':1, 'placeholder': 'MM/DD/YY'}), required=True)

	class Meta:
		model = Post
		fields = ['titulo', 'slug', 'intro', 'cuerpo', 'fecha']


class ComentarioForm(forms.ModelForm):
    
    class Meta:
        model = Comentario
        fields = ['nombre', 'email', 'cuerpo']