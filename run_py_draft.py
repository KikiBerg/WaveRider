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
    print("\nWelcome to WaveRider, your ultimate windsurfing companion!\n")
    print("Hey there, windsurfer! Hope you are you ready to conquer the waves today!\n")
    
    while True:  
        try:
            name = input("\n What's your name, Captain? ").upper()
            if not name.isalpha():
                raise ValueError("Whoa there, sailor! Names can only have letters (a-z).")
            
            while True:
                location = input(f"\nAhoy,{name}! Where are you anchored today? (e.g., City, Country)\n").upper()
                try:
                    city, country = location.strip().split(",")
                    city = city.strip()
                    country = country.strip()
                    if not city or not country:
                        raise ValueError("Looks like you forgot something, matey! Enter both city and country separated by a comma.\n")
                    break
                except ValueError:
                    print("Invalid location format. Did you mean something like 'Los Angeles, USA'? (enter city, country)\n")

            city_name = city # Extract city name into a variable           
            print(f"Splendid! {city_name} is such a beautiful place!\n") # Modify the code to only show the city in the welcome message
                                  
            break            

        except ValueError as err:
            print(f'{err}. Maybe the rum got the better of you? Try again.')
    return name, location # Return the location variable along with name


def windsurfing_skill(name, wind_sports):
    """Asks the user for their windsurfing skill level."""
    print(f"\nNow, let's get to know you better {name}")
    print(f"\n {name}, on a scale of 1 (chill surfer) to 10 (gnarly surfer), how would you rate your windsurfing skills?")
    skill_level = int(input("Choose your windsurfing spirit! Enter a number 1-10: \n"))    

    if skill_level <= 3: # Convert numerical skill level to categories
        skill_level = "Chill Surfer"
        wind_sports.append("cruising")
        print("Ah, a casual sailor! Lay back, soak up the sun and maybe catch a few waves.")
    elif skill_level <= 6:
        skill_level = "Freestyle Flyer"
        wind_sports.append("freestyle maneuvers")
        print("Feeling fancy? Get ready to show off those spins and jumps like a pro!")
    elif skill_level <= 10:
        skill_level = "Wave Slayer"
        wind_sports.append("catching waves")
        print("You hear the call of the ocean, don't you? Get ready to carve up those waves!")
    else:
        print(f"Woah there, {name}, that's beyond the scale! Are you whispering to the wind gods?\n")
        skill_level = "Legendary Windsurfer"
        wind_sports.append("anything you set your mind to")
        print("We salute you, legendary windsurfer! You can conquer any wind and wave!")
    
    print(f"Ok! Sounds like you're a {skill_level}! We'll check the conditions for {wind_sports[0]} today.")
    return skill_level, wind_sports # Return both skill level and wind_sports list


def get_windsurfing_suitability(temperature): # rename function get_water_and_temperature_tolerance
    """Asks the user for water and air temperature preferences,
    offering guidance on windsurfing suitability based on their input.
    Returns: 
    tuple: A tuple containing the user's water preference (str)
    and air temperature suitability (bool)."""
    print(f"\nNow, let's look a bit deeper at your preferences!")
    while True: # Get water preference with feedback
        preference = input("\nHow do you prefer the water for windsurfing? 'Warm' like a bath or 'cool' like a glacier?\n").lower()
        if preference in ("warm", "cool"):
            water_preference = preference
            if preference == 'warm':
                print(f"\nAh, a bathtub enthusiast! Perfect for practicing those mermaid impressions!")
            elif preference == 'cool':
                print(f"Excellent choice! Perfect for channeling your inner penguin (without the tuxedo).")                
            else:
                print(f"\nHold on, {preference} water? Hey there, landlubber! Those aren't water temperatures, those are shower settings. Try 'warm' or 'cool'.")
            break
    
    # Get air temperature tolerance and determine suitability
    print(f"\n Alright, {water_preference} water it is. Now, how do you handle air temperature?")
    tolerance = input("Would you define yourself as a 'tropical lizard' or a 'polar bear'?\n").lower()

    ideal_min_temp = 18 # Minimum ideal air temperature (Celsius)
    ideal_max_temp = 28 # Maximum ideal air temperature (Celsius)

    if tolerance in ("tropical lizard", "polar bear"):
        if tolerance == 'tropical lizard':
            ideal_min = 22
            ideal_max = 32
        elif tolerance == 'polar bear':
            ideal_min = 12
            ideal_max = 22
    else:
        print(f"Those aren't the only options {name}, but interesting choices! We'll assume you're adaptable.")
    
    if temperature  < ideal_min_temp:
        print("The air temperature is a bit chilly for windsurfing. Consider wearing a wetsuit or layering up.")
    elif temperature > ideal_max_temp:
        print("The air temperature might be a bit hot. Stay hydrated and consider sun protection.")
    else:
        print("The air temperature looks perfect for windsurfing!")     

    return water_preference, temperature >= ideal_min # Suitable if minimum threshold is met


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
        return weather, temperature, feels_like, wind_speed
    else:
        # Handle error: location not found, etc.
        print(f"An error occurred while fetching weather data for {location}.")
        return None, None, None, None    




def main():
    """ Run all program functions """
    name, location = welcome_user() # Unpack both name and location
    weather, temperature, feels_like, wind_speed = get_weather_data(api_key, location)  # Fetch weather data and unpack all

    if weather is None # Handle errors from get_weather_data
        return

    wind_sports = [] # Create an empty list to store windsports as examples of windsurfing activities for the chosen skill level    
    windsurfing_skill(name, wind_sports)  # Pass the empty list   
    water_pref, is_suitable = get_windsurfing_suitability(temperature) # Ask the user about water and air temp preferences and determine windsurfing suitability

    print(f"\nWindsurfing suitability based on your preferences:\n")
    print(f"  Water preference: {water_pref}\n")
    print(f"  Air temperature suitable: {is_suitable}\n")
    print(f"Some quick current weather facts for {location.split(',')[0].strip()}: The weather is {weather}. The temperature is {temperature}°C and it feels like {feels_like}°C. The wind speed is {wind_speed} m/s \n")
    

main()