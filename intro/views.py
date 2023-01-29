from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required()
def introduction(request):
    return HttpResponse('Hello')

def cars(request):
    context ={
        'all_cars': [
            {
                'brand': 'BMW',
                'color': 'Red',
                'year': 2022
            },
            {
                'brand': 'Dacia',
                'color': 'Blue',
                'year': 2021
            },
            {
                'brand': 'Audi',
                'color': 'Black',
                'year': 2020

            }
        ]
    }
    return render(request, 'intro/list_of_cars.html', context)

@login_required()
def movies(request):
    context ={
        'all_movies': [
            {
                'name':'Home Alone',
                'year': 2005,
                'rating': 9
            },
            {
                'name': 'Insidious',
                'year': 2012,
                'rating': 7
            },
            {
                'name': 'Polar Express',
                'year': 2008,
                'rating': 10
            },
            {
                'name': 'John Wick',
                'year': 2015,
                'rating': 6
            },
            {
                'name': 'Dominion',
                'year': 2004,
                'rating': 8
            }
        ]
    }
    return render(request, 'intro/list_of_movies.html', context)
