"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from inicio.views import inicio
from django.conf import settings
from django.conf.urls.static import static
from inicio.views import PostDetail, perfilDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', inicio.as_view(), name='inicio'),
    path('articulos', include('articulos.urls')),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('perfil_detail/<pk>', perfilDetail.as_view(), name='perfil_detail'),
    path('perfil_detail/<int:pk>/', perfilDetail.as_view(), name='perfil_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#+  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

