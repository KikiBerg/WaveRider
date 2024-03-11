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
            name = input("\n What's your name? ").upper()
            if not name.isalpha():
                raise ValueError("Name can only contain letters a-z.")
            
            while True:
                location = input(f"\nHi {name}! Where are you located? (e.g., City, Country)\n").upper()
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
            print(f"Now, let's get to know you better {name}")
            break            

        except ValueError as err:
            print(f'{err}. Please try again.')
    return name


def windsurfing_skill(name, wind_sports):
    """Asks the user for their windsurfing skill level."""
    print(f"\n {name}, on a scale of 1 (chill surfer) to 10 (gnarly surfer), how would you rate your windsurfing skills?")
    skill_level = int(input("Choose your windsurfing spirit! Enter a number 1-10: \n"))    

    if skill_level <= 3: # Convert numerical skill level to categories
        skill_level = "Chill Surfer"
        wind_sports.append("cruising")
        print("Imagine yourself effortlessly gliding across the water, soaking in the sun and the view.")
    elif skill_level <= 6:
        skill_level = "Freestyle Flyer"
        wind_sports.append("freestyle maneuvers")
        print("Feeling fancy? Tricks and jumps are perfect for showing off your moves and adding some flair to your ride.")
    elif skill_level <= 10:
        skill_level = "Wave Warrior"
        wind_sports.append("catching waves")
        print("Ready to ride the power of the ocean? Catching waves is all about timing and balance, the ultimate thrill for experienced surfers.")
    else:
        print(f"Woah there, {name}, that's beyond the scale! Maybe you're a windsurfing legend? \n")
        skill_level = "Legendary Windsurfer"
        wind_sports.append("anything you set your mind to")
        print("With your legendary skills, the possibilities are endless! Conquer any challenge the wind throws your way.")
    
    print(f"Sounds like you're a {skill_level}! We'll check the conditions for {wind_sports[0]} today.")
    return skill_level, wind_sports # Return both skill level and wind_sports list


def get_water_and_temperature_tolerance():
    """Asks the user for water temperature preference and tolerance for air temperature."""
    while True:
        preference = input("Do you prefer the water warm (like a bathtub) or cool (like a refreshing pool) for windsurfing? ").lower()
        if preference in ("warm", "cool"):
            water_preference = preference
            if preference == 'warm':
                print(f"\nAh, a bathtub enthusiast! Perfect for practicing those mermaid impressions!")
            elif preference == 'cool':
                print(f"Excellent choice! Perfect for channeling your inner penguin (without the tuxedo).")                
            else:
                print(f"\nHold on, {preference} water? Hey there, landlubber! Those aren't water temperatures, those are shower settings. Try 'warm' or 'cool'.")
            break
    
    print(f"\n Alright, {water_preference} water it is. Now, how do you handle air temperature?")
    tolerance = input("Would you define yourself as a 'tropical lizard' or a 'polar bear'?\n").lower()
    if tolerance not in ("tropical lizard", "polar bear"):
        print(f"Those aren't the only options {name}, but interesting choices! We'll assume you're adaptable.")
        tolerance = "adaptable"
    return water_preference, tolerance


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
        print(f"Some quick current weather facts for {location.split(',')[0].strip()}: The weather is {weather}. The temperature is {temperature}°C and it feels like {feels_like}°C. The wind speed is {wind_speed} m/s \n")
    else:
        # Handle error: location not found, etc.
        print(f"An error occurred while fetching weather data for {location}.")
        return None    




def main():
    """ Run all program functions """
    name = welcome_user() # Call welcome_user and store the returned name
    wind_sports = [] # Create an empty list to store windsports as examples of windsurfing activities for the chosen skill level
    windsurfing_skill(name, wind_sports)  # Pass the empty list   
    water_preference, tolerance = get_water_and_temperature_tolerance() # Get water tolerance after getting windsurfing skill
    

main()