'''
Created on Jul 23, 2014

@author: mcrisan
'''
import pprint
import tmdbsimple as tmdb
import ipdb
import datetime
from imdbpie import Imdb
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from django.conf import settings
from .tasks import movie_details, upcoming_movies, save_movies
from .forms import SearchForm
from .models import Category, Movie, Config
tmdb.API_KEY = settings.TMDB_API_KEY

#from imdbpie import Imdb 

def home(request, page=1):
    #save_movies.delay()
    #imdb = Imdb()
    #m=Movie.objects.first()
    #imdb.build_url(path, params)
    #data = imdb.find_movie_by_id(m.imdb_id)
    #ipdb.set_trace()
    movies = Movie.objects.filter(release_date__lte=datetime.datetime.now()).order_by('-release_date')
    movie = Paginator(movies, 18)
    conf = Config.objects.first()
    context = { "movies" : movie.page(page), 
                "page_nr" : page,
                "base_url": conf.base_url,
                "size": conf.size4}
    return render(request, "home.html", context)

def categories(request, category_id, page=1):
    try:
        category = Category.objects.get(tmdb_id=category_id)
    except:
        pass
    movies = category.movie_set.filter(release_date__lte=datetime.datetime.now()).order_by('-release_date')
    movie = Paginator(movies, 18)
    conf = Config.objects.first()
    context ={"movies": movie.page(page), 
              "category": category,
              "page_nr" : page,
              "base_url": conf.base_url,
              "size": conf.size4}
    return render(request, "category.html", context)


def movie_details(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except:
        pass
    
    conf = Config.objects.first()
    context ={"movie": movie,
              "base_url": conf.base_url,
              "size": conf.size4,
              "size1": conf.size7}
    return render(request, "movie_detail.html", context)

def search(request):
    if request.method == 'POST':       
        form = SearchForm(data=request.POST)
        if form.is_valid():
            conf = Config.objects.first()
            movies = Movie.objects.search(form.data['query'])
            context = { "movies" : movies, 
                       "query" : form.data['query'],
                       "base_url": conf.base_url,
                       "size": conf.size4,
                       "size1": conf.size7}
            return render(request, "search.html", context)
    else: 
        return redirect('movieapp:home')