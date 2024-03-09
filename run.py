# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import requests
from tkinter import *
import math
import random

api_key = "e33690fb74cac3d02cc1384e38f73c7d"

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
    return name


def windsurfing_skill(name, wind_sports):
    """Asks the user for their windsurfing skill level."""
    print(f"\n {name}, on a scale of 1 (chill surfer) to 10 (gnarly surfer), how would you rate your windsurfing skills?")
    skill_level = int(input("Choose your windsurfing spirit! (Enter a number 1-10): \n"))    

    if skill_level <= 3: # Convert numerical skill level to categories
        skill_level = "Chill Surfer"
        wind_sports.append("cruising")
    elif skill_level <= 6:
        skill_level = "Freestyle Flyer"
        wind_sports.append("freestyle maneuvers")
    elif skill_level <= 10:
        skill_level = "Wave Warrior"
        wind_sports.append("catching waves")
    else:
        print(f"Woah there, {name}, that's beyond the scale! Maybe you're a windsurfing legend? \n")
        skill_level = "Legendary Windsurfer"
        wind_sports.append("anything you set your mind to")
    
    print(f"Sounds like you're a {skill_level}! We'll check the conditions for {wind_sports[0]} today.")
    return skill_level, wind_sports # Return both skill level and wind_sports list


def get_weather_data(api_key, location):
    """Fetches weather data from Open Weather Map for the given location."""
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url).json() # convert it to a json in order to be able to access individual attributes
    
    if response['cod'] == 200: # Check if the request was successful
        # Extract and display relevant weather information here:

        weather = response['weather'][0]['main']
        temperature = response['main']['temp']        
        feels_like = math.floor(response['main']['temp'])
        wind_speed = response['wind']['speed']
        print(f"The weather in {location.split(',')[0].strip()} is currently: {weather}. The temperature is {temperature}°C and it feels like {feels_like}°C. The wind speed is {wind_speed} m/s \n")
    else:
        # Handle error: location not found, etc.
        print(f"An error occurred while fetching weather data for {location}.")
        return None    




def main():
    """ Run all program functions """
    name = welcome_user() # Call welcome_user and store the returned name
    wind_sports = [] # Create an empty list to store windsports as examples of windsurfing activities for the chosen skill level
    windsurfing_skill(name, wind_sports)  # Pass the empty list
    

main()