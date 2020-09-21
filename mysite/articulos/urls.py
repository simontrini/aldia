from . import views
#from django.conf.urls import url
from django.urls import path
#from django.conf.urls import url, include

urlpatterns = [
  path('', views.PostList.as_view(), name='home'),
  path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
  #path('id/', views.perfilDetail.as_view(), name='perfil_detail'),
]

#urlpatterns = [
    #url(r'^$', views.PostList.as_view(), name='PostList'),
    ##url(r'<slug:slug>/', views.PostDetail, name='PostDetail'),
    ##url(r'^<slug:slug>/, views.PostDetail, name='PostDetail'),
    #url(r'^(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='PostDetail'),
#]
