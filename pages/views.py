from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }

    return render(request, 'pages/index.html', context=context)

def about(request):
    return render(request, 'pages/about.html')