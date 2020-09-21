# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


STATUS = (
    (0,"Edicion"),
    (1,"Publicado")
)
#RED = (
    #(0,"Facebook"),
    #(1,"Imstagram"),
    #(2,"twitter")
#)

#from django.contrib.auth.models import User

class perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to="articulos", null=True, blank=True,
        verbose_name="Imagen")
    telefono = models.CharField(max_length=200)
    
class etiquetaP(models.Model):
    texto = models.CharField(max_length=200)
    #tipo = models.IntegerField(choices=RED, default=0)
    def __str__(self):
        return "{}".format(self.texto)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='+')
    etiquetaP = models.ForeignKey(etiquetaP, on_delete= models.CASCADE, verbose_name="Etiqueta Principal",default=0)
    subido_on = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    creado_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to="articulos", null=True, blank=True,
        verbose_name="Imagen")

    class Meta:
        ordering = ['-creado_on']

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)