from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artists/", views.artists, name="artists"),
    path("artist/<int:artist_id>/",
        views.artist_info, name="artist_info"),
    path("album/<int:album_id>/", views.album_info, name="album_info"),
    path("song/<int:song_id>/", views.song_info, name="song_info")
]