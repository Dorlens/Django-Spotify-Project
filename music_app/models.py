from django.db import models

# Create your models here.

class Music_tracks(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    #genre = models.CharField(max_length=100,blank=True, null=True)
    preview_url = models.URLField(null=True, blank=True)
    cover_image = models.URLField()
    like_song =models.BooleanField(default=False)
    dislike_song =models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} by {self.artist}"