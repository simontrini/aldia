# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    print("hola mundo")
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-creado_on')
    template_name = 'listaDePost.html'
    #queryset = Post.objects.filter(status='1')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detalleDePost.html'