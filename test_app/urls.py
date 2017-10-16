from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_cat/$', views.create_cat, name='create_cat'),
    url(r'^info_book/$', views.info_book, name='info_book'),

]
