
from django.shortcuts import render
from tpb import TPB
from tpb import ORDERS
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import Movie



def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Test </h1>")
    return render(request, "home.html", {})

def movies_view(request, *args, **kwargs):
    return render(request, "movies.html", {})

@csrf_exempt
def movie_lookup(request, movie):
   
    website = TPB("https://thepiratebay.org/") #Base URL for ThePirateBay
    
    counter = 0
    obj = {}

    for torrent in website.search(movie).order(ORDERS.SEEDERS.DES):
        if counter <= 2:
            temp = Movie(title= str(torrent.title), magnet=str(torrent.magnet_link))
            temp.save()
            temp_movie = Movie.objects.get(id=temp.id)
            obj["movie" + str(counter + 1)] = temp_movie
        counter += 1
        
    return render(request, "movies.html", obj)
