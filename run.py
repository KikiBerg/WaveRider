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
    """Greets the user welcome and asks for their name."""
    print("Welcome to WaveRider! Your ultimate companion for conquering the windswept waves with finesse and confidence.\n")
    while True:
        name = input("Hey there, windsurfer! What's your name? ")

        try:
            if name.isalpha():                
                print(f"Welcome to WaveRider, {name}!\n")
                location = input(f"{name}, where are you located? (e.g., City, Country)\n")
                print(f"Wow, {location} is such a nice place!\n")                
                get_weather_data(api_key, location)  # Call get_weather_data function with user-provided location
                break                                   
            elif len(name) == 0:
                print("Why not provide a name?")
            else:
                print(f"{name} is invalid. You can only enter letters a-z\n")
        except ValueError as err:
            print(f'{err}. Please try again.')                 


def get_weather_data(api_key, location):
    """Fetches weather data from Open Weather Map for the given location."""
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url).json() # convert it to a json in order to be able to access individual attributes
    
    if response['cod'] == 200: # Check if the request was successful (response code 200)
        # Extract and display relevant weather information here, e.g:

        weather = response['weather'][0]['main']
        temperature = response['main']['temp']
        print(f"The weather in {location} is currently {weather}. The temperature is {temperature}°C.")
    else:
        # Handle error: location not found, etc.
        print(f"An error occurred while fetching weather data for {location}.")
    


welcome_user()
