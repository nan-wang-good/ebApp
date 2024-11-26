from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    # /movie/
    path('', views.index, name='index'),
    # /movie/id e.g. /movie/1
    path('<int:movie_id>/', views.show, name='show'),

]

