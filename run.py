# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import requests
from tkinter import *
import math
import random

api_key = "e33690fb74cac3d02cc1384e38f73c7d"
#location = "Stockholm, SE"

def welcome_user():
    """Greets the user welcome, asks for their name and location and validates input."""
    print("Welcome to WaveRider, your ultimate windsurfing companion!\n")
    print("Hey there, windsurfer! Are you ready to conquer the waves today?\n")
    
    while True:  
        try:
            name = input("What's your name? ").upper()
            if not name.isalpha():
                raise ValueError("Name can only contain letters a-z.")
            
            while True:
                location = input(f"{name}, where are you located? (e.g., City, Country)\n").upper()
                try:
                    city, country = location.strip().split(",")
                    city = city.strip()
                    country = country.strip()
                    if not city or not country:
                        raise ValueError("Please enter both city and country separated by a comma.\n")
                    break
                except ValueError:
                    print("Invalid location format. Please enter: 'City, Country'.\n")

            city_name = city # Extract city name into a variable           
            print(f"Splendid! {city_name} is such a beautiful place!\n") # Modify the code to only show the city in the welcome message
            get_weather_data(api_key, location)
            break            

        except ValueError as err:
            print(f'{err}. Please try again.') 


def get_weather_data(api_key, location):
    """Fetches weather data from Open Weather Map for the given location."""
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url).json() # convert it to a json in order to be able to access individual attributes
    
    if response['cod'] == 200: # Check if the request was successful (response code 200)
        # Extract and display relevant weather information here:

        weather = response['weather'][0]['main']
        temperature = response['main']['temp']        
        feels_like = math.floor(response['main']['temp'])
        print(f"The weather in {location.split(',')[0].strip()} is currently: {weather}. The temperature is {temperature}°C and it feels like {feels_like}°C")
    else:
        # Handle error: location not found, etc.
        print(f"An error occurred while fetching weather data for {location}.")
    




def main():
    """ Run all program functions """
    welcome_user()
    
print("")
main()