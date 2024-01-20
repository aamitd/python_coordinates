import os
from geopy.geocoders import Nominatim
from colorama import Fore, Style
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the user_email from environment variables
user_email = os.getenv("USER_EMAIL")

# Path to the file containing coordinates
file_path = '/Users/amitdahan/PycharmProjects/Coordinates/coordi'


def get_address(latitude, longitude):
    try:
        # Initialize geolocator with the user's email as user agent
        geolocator = Nominatim(user_agent=user_email)
        # Reverse geocode to get address from latitude and longitude
        location = geolocator.reverse((latitude, longitude), language='en')

        return location.address if location else None

    except Exception as e:
        print(f"Error: ", e)
        return None


# Desired locations to search for in the address
desired_locations = ['HaArbaa', 'Hod Hasharon']

# Read coordinates from the file
with open(file_path, 'r') as file:
    content = file.readlines()

    for line in content:
        # Skip empty lines
        if not line.strip():
            continue

        # Split each line into latitude and longitude
        lat, lon = map(float, line.strip().split(','))

        # Call the get_address function for each pair
        address = get_address(lat, lon)

        # Check if the address contains any of the desired locations
        if address and any(location.lower() in address.lower() for location in desired_locations):
            # Print the address with formatting
            print(f"The address of the coordinates {lat}, {lon} is: {Fore.RED}{Style.BRIGHT}{address}{Style.RESET_ALL}")

