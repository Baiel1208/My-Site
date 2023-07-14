from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, 'blablacar/index.html')

def poputchik(request):
    return render(request, 'blablacar/poputchik.html')
def bus(request):
    return render(request, 'blablacar/bus.html')

def search_car(request):
    return render(request, 'blablacar/search_car.html')


def offer_seats(request):
    return render(request, 'blablacar/offer_seats.html')