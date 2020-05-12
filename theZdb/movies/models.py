from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Poster(models.Model):
    title = models.CharField(max_length=20)
    lang = models.CharField(max_length=3)
    image = models.ImageField(upload_to='posters')

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    direcor = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    posters = models.ManyToManyField(Poster, blank=True)

    def __str__(self):
        return self.title