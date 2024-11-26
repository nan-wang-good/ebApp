# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse("You're at the movie index.")
#------------------After add movie template---------------------------
from django.shortcuts import render
from .models import Movie
from django.http import Http404

def index(request):
    newest_movies = Movie.objects.order_by('-release_date')[:15]
    context = {'newest_movies': newest_movies}
    return render(request, 'movie/index.html', context)
    
def show(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, 'movie/show.html', {'movie': movie})
    



