from django.contrib import admin
from .models import Tag, Poster, Movie
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass

class PosterAdmin(admin.ModelAdmin):
    pass

class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', 'posters')

admin.site.register(Tag, TagAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Movie, MovieAdmin)