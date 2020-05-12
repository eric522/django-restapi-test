from django.urls import path
from .views import TagList, TagDetail, PosterList, PosterDetail, MovieList, MovieDetail

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('posters/', PosterList.as_view(), name='poster-list'),
    path('posters/<int:pk>/', PosterDetail.as_view(), name='poster-detail'),
]