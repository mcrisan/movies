from __future__ import absolute_import

import datetime
import pprint

import tmdbsimple as tmdb
import ipdb
from datetime import timedelta
from django.db.models import Max, Count
from imdbpie import Imdb

from django.conf import settings
from celery import shared_task
from .models import Category, Movie, Video, Image, Keyword, Config

tmdb.API_KEY = settings.TMDB_API_KEY


@shared_task
def save_categories():
    print "adding categories"
    genres = tmdb.Genres()
    genre_list = genres.list() 
    cat_ids = [category.tmdb_id for category in Category.objects.all()]
    for genre in genre_list['genres']:
        if genre['id'] not in cat_ids:
            cat = Category(tmdb_id=genre['id'], name=genre['name']) 
            cat.save()
            
@shared_task
def save1_categories():
    print "adding categories"
    genres = tmdb.Genres()
    genre_list = genres.list() 
    cat_ids = [category.tmdb_id for category in Category.objects.all()]
    for genre in genre_list['genres']:
        if genre['id'] not in cat_ids:
            cat = Category(tmdb_id=genre['id'], name=genre['name']) 
            cat.save()
            
@shared_task
def save_movies():
    print "adding movies"
    categories = Category.objects.all()
    for cat in categories:
        genres = tmdb.Genres(cat.tmdb_id)
        movies = genres.movies(include_all_movies=True) 
        pages = movies['total_pages']
        for i in range(1, pages+1):
            movies = genres.movies(page=i)
            for movie in movies['results']:
                new_movie = Movie.save_movie(movie) 
                if new_movie:
                    movie_details(new_movie)
                    add_videos(new_movie)
                    add_images(new_movie)
                    add_keywords(new_movie)
    
def movie_details(movie):
    print "movie_details"
    tmdb_movies = tmdb.Movies(movie.tmdb_id)
    info = tmdb_movies.info()
    movie.update_movie(info)
        
def add_videos(movie):
    print "videos"
    tmdb_movies = tmdb.Movies(movie.tmdb_id)
    videos = tmdb_movies.videos()
    for video in videos['results']:
        if not Video.objects.filter(key=video['key']).exists():
            vid = Video(key=video['key'], 
                        name=video['name'],
                        site=video['site'],
                        type=video['type'],
                        size=video['size'],
                        movie=movie)
            try:
                vid.save()
            except:
                print "video except"
                
def add_images(movie):
    print "images"
    tmdb_movies = tmdb.Movies(movie.tmdb_id)
    images = tmdb_movies.images()
    for image in images['backdrops']:
        if not Image.objects.filter(file_path=image['file_path']).exists():
            img = Image(file_path=image['file_path'], 
                        width=image['width'],
                        height=image['height'],
                        vote_average=image['vote_average'],
                        vote_count=image['vote_count'],
                        movie=movie)
            try:
                img.save()
            except:
                print "image except"
                
def add_keywords(movie):
    print "keywords"
    tmdb_movies = tmdb.Movies(movie.tmdb_id)
    keywords = tmdb_movies.keywords()
    for keyword in keywords['keywords']:
        if not Keyword.objects.filter(tmdb_id=keyword['id']).exists():
            key = Keyword(tmdb_id=keyword['id'],
                          name=keyword['name'])
            try:
                key.save()
                movie.keywords.add(key)
            except:
                print "image except"
                
@shared_task                
def upcoming_movies():
    tmdb_movies = tmdb.Movies()
    movies = tmdb_movies.upcoming()
    pages = movies['total_pages']
    for i in range(1, pages+1):
        movies = tmdb_movies.upcoming(page=i)
        for movie in movies['results']:
            new_movie = Movie.save_movie(movie) 
            if new_movie:
                movie_details(new_movie)
                add_videos(new_movie)
                add_images(new_movie)
                add_keywords(new_movie)
            else:
                print "este nul"    
                
@shared_task                
def save_config():
    print "config"
    conf = tmdb.Configuration()
    conf_data = conf.info()
    config = Config.objects.first()
    if not config:
        config = Config()
    config.base_url = conf_data['images']['base_url']
    config.size1 = conf_data['images']['poster_sizes'][0]
    config.size2 = conf_data['images']['poster_sizes'][1]
    config.size3 = conf_data['images']['poster_sizes'][2]
    config.size4 = conf_data['images']['poster_sizes'][3]
    config.size5 = conf_data['images']['poster_sizes'][4]
    config.size6 = conf_data['images']['poster_sizes'][5]
    config.size7 = conf_data['images']['poster_sizes'][6]
    config.save()
        

    

        
    
          
                             
        