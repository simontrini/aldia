# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from articulos.models import Post, perfil

class inicio(generic.ListView):
    model = Post
    template_name = 'inicio.html'
    #queryset = Post.objects.filter(status='1')
    def get_context_data(self, **kwargs):
        context = super(inicio, self).get_context_data(**kwargs)
        context['noticias2'] =[{"imagen":"imagenes/merilimpioSolidario.jpg","titulo":"otra imagen1",},
                               {"imagen":"imagenes/merilimpioSolidario.jpg","titulo":"otra imagen2",},
                               {"imagen":"imagenes/merilimpioSolidario.jpg","titulo":"otra imagen3",},
                               {"imagen":"imagenes/merilimpioSolidario.jpg","titulo":"otra imagen4",},
                              ]
        context['noticias1'] = Post.objects.filter(status=1).order_by('-creado_on')
        return context

#def inicio(request):
    #return render(request, 'inicio.html', {'poll': 'hola'})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detalle.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['noticias1'] = Post.objects.filter(status=1).order_by('-creado_on')

        return context

class perfilDetail(generic.DetailView):
    model = perfil
    template_name = 'perfilDetalle.html'
    queryset = perfil.objects.filter(pk='1')
    def get_context_data(self, **kwargs):
        context = super(perfilDetail, self).get_context_data(**kwargs)
        context['noticias1'] = Post.objects.filter(status=1).order_by('-creado_on')

    #return context

    #def get_context_data(self, **kwargs):
        #context = super(PostDetail, self).get_context_data(**kwargs)
        ##context['productos'] = Producto.objects.filter(status=1).order_by('-creado_on')
        #return context