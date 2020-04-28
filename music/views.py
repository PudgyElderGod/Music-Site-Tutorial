from django.shortcuts import render
from django.http import HttpResponse

from .models import Artist, Album, Song

# Create your views here.

def index(request):
    # return render(request, "index.html", context)
    return HttpResponse("Welcome to the music site! Navigate to /artists to get started!")

def artists(request):
    context = {
        "artists": Artist.objects.all()
    }
    return render(request, "artists.html", context)

def artist_info(request, artist_id):
    context = {
        "artist": Artist.objects.get(id=artist_id),
        "albums": Album.objects.filter(artist=artist_id)
    }
    return render(request, "artist_info.html", context)

def album_info(request, album_id):
    context = {
        "album": Album.objects.get(id=album_id),
        "songs": Song.objects.filter(album=album_id)
    }
    return render(request, "album_info.html", context)

def song_info(request, song_id):
    context = {
        "song": Song.objects.get(id=song_id)
    }
    return render(request, "song_info.html", context)