from django.urls import path

from intro import views

urlpatterns = [
    path('introduction/', views.introduction, name='introduction'),
    path('list_of_cars/', views.cars, name='list-of-cars'),
    path('list_of_movies/', views.movies, name='list-of-movies'),

]