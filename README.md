# Geocoding Coordinates Python Script

This Python script leverages the Geopy library to perform reverse geocoding, converting latitude and longitude coordinates into human-readable addresses using the Nominatim geocoder. 

## Prerequisites

Before running the script, ensure you have the necessary libraries installed. You can install them using the following command:

```bash
pip3 install geopy
```

```bash
pip3 install colorama
```

```bash
pip3 install python-dotenv
```

ensure that you change the file_path to yours path


## 1. Coordinate Geocoding Function:

The script defines a function named get_address that takes latitude and longitude coordinates as input and utilizes the Nominatim geolocator to obtain the corresponding address.
The function handles exceptions, printing error messages if any issues arise during the geocoding process.

## 2. Desired Locations List:

The script specifies a list of desired locations, such as 'HaArbaa' and 'Hod Hasharon,' which will be used to search for matching addresses.

## 3. File Reading and Iteration:

The script reads coordinates from a file specified by file_path.
For each line in the file, the script extracts latitude and longitude values and calls the get_address function.

## 4. Address Matching and Output:

The script checks if the obtained address contains any of the desired locations, regardless of case.
If a match is found, the address is printed.

## Usage:
The script is designed to read a file containing coordinates, geocode them to obtain addresses, and search for specific locations in the addresses.
The desired locations can be customized by modifying the desired_locations list.
