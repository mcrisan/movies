import datetime

from django.db import models

class Category(models.Model):
    tmdb_id = models.IntegerField("TMDB ID", unique=True)
    name = models.CharField("Name", max_length=70)
    
    def __unicode__(self):  
        return self.name
    
class Keyword(models.Model):
    tmdb_id = models.IntegerField("TMDB ID", unique=True)
    name = models.CharField("Name", max_length=70)
    
    def __unicode__(self):  
        return self.name
 
 
class MovieManager(models.Manager):  
    def search(self, query):
        return self.filter(title__icontains=query)
    
        
class Movie(models.Model):
    tmdb_id = models.IntegerField("TMDB ID", unique=True)
    original_title = models.CharField(max_length=250)
    release_date = models.DateField(default=datetime.datetime.now())
    poster_path = models.CharField(max_length=250)
    backdrop_path = models.CharField(max_length=250, default=None, null=True, blank=True)
    title = models.CharField(max_length=250)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    categories = models.ManyToManyField(Category)
    keywords = models.ManyToManyField(Keyword, null=True, blank=True)
    imdb_id = models.CharField(max_length=250, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    tagline = models.TextField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    
    objects = MovieManager()
    
    @classmethod
    def exists(cls, tmbd_movie_id):
        return cls.objects.filter(tmdb_id=tmbd_movie_id).exists()
    
    @classmethod
    def save_movie(cls, movie):
        db_movie = cls.objects.filter(tmdb_id=movie['id']).first()
        if not db_movie:
            new_movie = Movie(tmdb_id=movie['id'], 
                          original_title=movie['original_title'],
                          release_date=movie['release_date'],
                          poster_path=movie['poster_path'],
                          title=movie['title'],
                          vote_average=movie['vote_average'],
                          vote_count=movie['vote_count'],
                          )
            try: 
                new_movie.save()
                return new_movie
            except:
                print "inca o excepie"
                return 
        else:
            return  db_movie 
        
    def update_movie(self, info):
        for genre in info['genres']:
            if not self.has_cat(genre['id']):
                try:
                    cat = Category.objects.get(tmdb_id=genre['id'])
                except:
                    cat = Category(tmdb_id=genre['id'], name =genre['name'] )
                self.categories.add(cat)
        self.imdb_id = info['imdb_id']
        self.popularity = info['popularity']
        self.revenue = info['revenue']
        self.runtime = info['runtime']
        self.tagline = info['tagline']
        self.budget = info['budget']
        self.backdrop_path = info['backdrop_path']  
        try:
            self.save()   
        except:
            pass      
    
    def has_cat(self, cat_id):
        return self.categories.filter(tmdb_id=cat_id).exists()
    
    def __unicode__(self):  
        return self.title  
    

class Video(models.Model):
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    size = models.IntegerField()
    movie = models.ForeignKey(Movie, default=None, null=True, blank=True) 
    
class Image(models.Model):
    file_path = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    movie = models.ForeignKey(Movie, default=None, null=True, blank=True) 
    

class Config(models.Model):
    base_url = models.CharField(max_length=200)
    size1 = models.CharField(max_length=20)
    size2 = models.CharField(max_length=20)
    size3 = models.CharField(max_length=20)
    size4 = models.CharField(max_length=20)
    size5 = models.CharField(max_length=20)
    size6 = models.CharField(max_length=20)
    size7 = models.CharField(max_length=20)
    
        

    