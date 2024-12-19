# Copyright 2024, Sandro Ribeiro. All rights reserved.

import requests
import time

def format_location(address):

    """
    Formats the location name based on the 
    address data.
    """ 

    suburb = address.get("suburb", "Unknown_suburb")
    city = address.get("city", "Unknown_city")
    state = address.get("state", "Unknown_state")

    return [suburb, city, state]



def get_location_name(lat, lon):

    """
    Uses the Nominatim API to retrieve and format 
    the location name from coordinates.
    """
    print(f"Requesting location for Coordinates: Latitude = {lat}, Longitude = {lon}")

    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json"
    }
    headers = {
        "User-Agent": "PhotoOrganizer/1.0 (santunesribeiro@outlook.com)"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        print(f"API Response Status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            address = data.get("address", {})
            location = format_location(address)
            print(f"Location Found: {location}")
            return location
           
        elif response.status_code == 429:
            print("Rate limit exceeded. Retrying after a delay...")
            time.sleep(1)
            return get_location_name(lat, lon)
        
        else:
            print(f"Unexpected API Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error while connecting to the API: {e}")
    
    return "Unknown Location"
