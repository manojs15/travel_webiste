from django.db import models

class TravelBooking(models.Model):
    total_people = models.IntegerField()
    vehicle_type = models.CharField(max_length=100)
    seat_capacity = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    places_to_visit = models.TextField()
    phone_number = models.BigIntegerField()  # Storing phone number as a complete integer

    def __str__(self):
        return f"Booking for {self.total_people} people - {self.vehicle_type}"
