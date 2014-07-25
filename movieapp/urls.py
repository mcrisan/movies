'''
Created on Jul 23, 2014

@author: mcrisan
'''
from django.conf.urls import patterns, include, url

from movieapp import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'), 
    url(r'^page(?P<page>[0-9]+)/$', views.home, name='home_pag'),
    url(r'category/(?P<category_id>\d+)/$', views.categories, name='categories'),
    url(r'category/(?P<category_id>\d+)/page(?P<page>[0-9]+)/$', views.categories, name='categories_page'),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie_details, name='movie_details'),
    url(r'^search/$', views.search, name='search'),
)
