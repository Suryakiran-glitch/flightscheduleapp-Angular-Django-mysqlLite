from django.db import models

# Create your models here.
class Schedule(models.Model):
    airline = models.CharField(max_length=200)
    flight_no = models.CharField(max_length=50)
    trip_type = models.CharField(max_length=50)
    departure_airport = models.CharField(max_length=50)
    arrival_airport = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

