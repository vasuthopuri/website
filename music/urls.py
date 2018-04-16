from django.conf.urls import url
from music import views




app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^resume/$', views.resume, name='resume'),

]
