from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Ensure a user exists
        if not User.objects.exists():
            User.objects.create_user(username='admin', email='admin@example.com', password='password')

        user = User.objects.first()

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                price_per_night=random.randint(50, 500),
                location=fake.city(),
                host=user
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
