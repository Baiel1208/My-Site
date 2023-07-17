from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Trip(models.Model):
    start_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='trips_from', verbose_name="Откуда")
    end_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='trips_to', verbose_name="Куда")
    # created = models.DateField(auto_now=True, verbose_name="Дата публикации")
    seats_available = models.IntegerField()
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

class Booking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')


