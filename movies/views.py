from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Movie

# Create your views here.

def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }

    return render(request, 'movies/movies.html', context=context)

def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk = movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404('Sayfa Bulunamadı')

    movie = get_object_or_404(Movie, pk=movie_id)

    context = {
        'movie' : movie
    }

    return render(request, 'movies/detail.html', context=context)

def search(request):
    return render(request, 'movies/search.html')