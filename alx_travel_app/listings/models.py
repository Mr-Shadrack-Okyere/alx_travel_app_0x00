Listing

title, description, price_per_night, location

host → ForeignKey to User

created_at → timestamp

Booking

listing → ForeignKey to Listing

user → ForeignKey to User

start_date, end_date, total_price

created_at → timestamp

Review

listing → ForeignKey to Listing

user → ForeignKey to User

rating, comment

created_at → timestamp

from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
