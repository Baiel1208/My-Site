from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blablacar.forms import TripForm
from blablacar.models import Trip


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


class PostCreateViews(generic.CreateView):
    model = Trip
    form_class = TripForm
    template_name = "blablacar/offer_seats.html"
    # fields = ['title', 'content','cover', "status"]
    success_url = reverse_lazy("index-page")

