from django.urls import path

from blablacar import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("poputchik/", views.poputchik, name="poputchik-page"),
    path("bus/", views.bus, name="bus-page"),
    path("search-car-sharing/", views.search_car, name="search-car-page"),
    path("offer-seats/", views.offer_seats, name="offer-seats-page"),
]