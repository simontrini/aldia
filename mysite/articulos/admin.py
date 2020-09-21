# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, etiquetaP, perfil

class PostAdmin(SummernoteModelAdmin):
#class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status','creado_on')
    list_filter = ("status",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    summernote_fields = ('contenido',)

    #summernote_fields = '__all__'

admin.site.register(Post, PostAdmin)

@admin.register(etiquetaP)
class etiquetaPAdmin(admin.ModelAdmin):
    list_display = ('texto',)
    list_filter = ("texto",)
    search_fields = ['texto',]

#@admin.register(perfil, PerfilAdmin)
class PerfilAdmin(SummernoteModelAdmin):
#class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio',)
    #list_filter = ("status",)
    search_fields = ['user', 'bio']
    #prepopulated_fields = {'slug': ('titulo',)}
    summernote_fields = ('bio',)
    
admin.site.register(perfil, PerfilAdmin)  

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField()
    #image = models.ImageField(upload_to="articulos", null=True, blank=True,
        #verbose_name="Imagen")
        #verbose_name="Imagen")
    #telefono = models.CharField(max_length=200)    