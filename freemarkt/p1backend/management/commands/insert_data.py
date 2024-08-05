import random
import string
from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from p1backend.models import Contact

# Lists of common Indian first names and surnames
first_names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan", "Mohan", "Radheshyam", "Jignesh", "Shakti", "Arya", "Amrut", "Romesh", "Mayank"]
surnames = ["Sharma", "Verma", "Gupta", "Mehta", "Patel", "Reddy", "Chauhan", "Rajput", "Singh", "Kumar", "Jadhav", "Chavan", "Dhargalkar", "Netravalkar", "Joshi", "Jagtap", "Nalawade", "Nimbalkar", "Bhosale"]

# Function to generate a random mobile number
def generate_mobile():
    return "9" + ''.join(random.choices(string.digits, k=9))

# Function to generate a random email ID
def generate_email(name):
    domains = ["gmail.com", "yahoo.com", "outlook.com", "rediffmail.com", "aol.com", "protonmail.com"]
    return f"{name.lower().replace(' ', '')}@{random.choice(domains)}"

# Function to generate a random address in India
def generate_address():
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Surat"]
    return f"{random.randint(1, 500)}, {random.choice(cities)}"

# Function to generate a random GPS location within India
def generate_gps():
    lat = round(random.uniform(8.4, 37.6), 6)
    lon = round(random.uniform(68.7, 97.25), 6)
    return Point(lon, lat)

class Command(BaseCommand):
    help = 'Generate dummy farmers data and save it to the database'

    def handle(self, *args, **kwargs):
        # Generate 1000 dummy records
        for _ in range(100):
            first_name = random.choice(first_names)
            surname = random.choice(surnames)
            full_name = f"{first_name} {surname}"
            mobile = generate_mobile()
            address = generate_address()
            gps_location = generate_gps()
            email = generate_email(full_name)

            # Create and save a new Contact object
            Contact.objects.create(
                name=full_name,
                mobile=mobile,
                address=address,
                gps_location=gps_location,
                email=email
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))


