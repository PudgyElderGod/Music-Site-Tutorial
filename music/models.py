from django.db import models

#Models here
class Artist(models.Model):
    name = models.CharField(max_length=50)
    formation_date = models.DateField(blank=True, null=True)
    blurb = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title