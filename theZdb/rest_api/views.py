from rest_framework import generics, views, status
from django.http import Http404
from rest_framework.response import Response 
from .serializers import Tag, Poster, Movie, TagSerializer, PosterSerializer, MovieSerializer 
# Create your views here.

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(views.APIView):

    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class PosterList(generics.ListAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterDetail(views.APIView):

    def get_object(self, pk):
        try:
            return Poster.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        poster = self.get_object(pk)
        serializer = PosterSerializer(poster, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(views.APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)