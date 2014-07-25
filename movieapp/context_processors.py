import pprint 
import ipdb

import tmdbsimple as tmdb
from django.conf import settings
from .models import Category

tmdb.API_KEY = settings.TMDB_API_KEY
                   
def load_categories(request):     
    categories = Category.objects.all()
    context={'categories': categories}
    return context
