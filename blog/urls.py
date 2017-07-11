from django.conf.urls import include, url
from . import views
from votes import urls


urlpatterns = [
        url(r'^$', views.ingresar),
		url(r'^privado/post_list$', views.post_list, name='listado'),
        url(r'^privado/alumnos$', views.post_list_alumnos),
        url(r'^privado/profesores$', views.post_list_profesores),
        url(r'^privado/otros$', views.post_list_otros),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^usuario/nuevo$', views.nuevo_usuario, name='nuevo_usuario'),
        url(r'^privado/$', views.privado),
        url(r'^cerrar/$', views.cerrar),
        url(r'^privado/tusposteos$', views.post_list_privado),
        url(r'^privado/tusposteos/post/(?P<pk>[0-9]+)/$', views.post_detail_privado),
		url(r'^mejores_semanales$', views.post_list_mejores_semanales),
		url(r'^mejores_mensuales$', views.post_list_mejores_mensuales),
        url(r'^$', include(urls)),
]

