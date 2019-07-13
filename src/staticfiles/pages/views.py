from django.http import HttpResponse
from django.shortcuts import render
from tpb import TPB
from tpb import CATEGORIES, ORDERS
from django.db import models

# Create your views here.

from .models import Movie



def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Test </h1>")
    return render(request, "home.html", {})

def movies_view(request, *args, **kwargs):
    return render(request, "movies.html", {})

def movie_lookup(request, movie):

    website = TPB("https://thepiratebay.org/")
    
    for torrent in website.search(movie):
        print(torrent.url)
    
    temp = Movie(title=str(movie), length="test", url="Test")
    temp.save()

    temp_movie = Movie.objects.get(id=temp.id)
    obj = {
        "object": temp_movie
    }
    print(temp_movie.url)

    return render(request, "base.html", obj)
