# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import requests
import time
import math
import random
import pyfiglet

api_key = "e33690fb74cac3d02cc1384e38f73c7d"


def wave_rider_ascii():
    """
    A welcome ascii art for WaveRider
    """
    welcome_text_ascii = "Wave Rider"
    wave_rider_ascci_art = pyfiglet.figlet_format(
        welcome_text_ascii, font='speed', justify='center'
    )
    print(wave_rider_ascci_art)


def welcome_user():
    """
    Greets the user welcome, asks for their
    name and location and validates input.
    """
    print("Welcome to WaveRider, your ultimate windsurfing"
          "companion!\n")
    print("Hey there, windsurfer! Hope you are you ready "
          "to conquer the waves today!\n")

    while True:
        try:
            name = input("\n What's your name, Captain? ").upper()
            if not name.isalpha():
                raise ValueError("Whoa there, sailor!"
                                 " Names can only have letters (a-z).")
            while True:
                location = input(f"\nAhoy,{name}! Where are you anchored"
                                 f" today? (e.g., City, Country)\n").upper()
                try:
                    city, country = location.strip().split(",")
                    city = city.strip()
                    country = country.strip()
                    if not city or not country:
                        raise ValueError("Well matey, you need to enter"
                                         " both city and country separated"
                                         " by a comma.\n")
                    break
                except ValueError:
                    print("Did you mean something like 'Los Angeles, US'?"
                          " (Enter: city, country)\n")

            city_name = city  # Extract city name into a variable
            # Show only the city in the welcome message
            print(f"Splendid! {city_name} is such a beautiful place!\n")
            time.sleep(1)

            break

        except ValueError as err:
            print(f'{err}. Maybe the rum got the better of you? Try again.')
    return name, location  # Return the location variable along with name


def windsurfing_skill(name, wind_sports):
    """Asks the user for their windsurfing skill level."""
    time.sleep(5)
    print(f"\nNow, let's get to know you better {name}")
    print(f"\n {name}, on a scale of 1 to 10, how would you"
          f" rate your windsurfing skills?")
    print(f"\n 1: chill surfer and 10: gnarly surfer")
    print(f"\n p.s The sky is the limit; so greater numbers apply too!")
    skill_level = int(input("Choose your windsurfing spirit!"
                            " Enter a number: \n"))

    if skill_level <= 3:  # Convert numerical skill level to categories
        skill_level = "Chill Surfer"
        wind_sports.append("cruising")
        print("Ah, a casual sailor! Lay back, soak up the sun"
              " and maybe catch a few waves.")
    elif skill_level <= 6:
        skill_level = "Freestyle Flyer"
        wind_sports.append("freestyle maneuvers")
        print("Get ready to show off those"
              " spins and jumps like a pro!")
    elif skill_level <= 10:
        skill_level = "Wave Slayer"
        wind_sports.append("catching waves")
        print("You hear the call of the ocean, don't you?"
              " Get ready to carve up those waves!")
    else:
        print(f"Woah there, {name}, that's beyond the scale!"
              f" Are you whispering to the wind gods?\n")
        skill_level = "Legendary Windsurfer"
        wind_sports.append("anything you set your mind to")
        print("We salute you, legendary windsurfer!")

    print(f"Ok {name}, looks like you're a {skill_level}!"
          f" We'll soon check today's wind conditions for {wind_sports[0]}.")
    print("Remember, even if the wind isn't perfect, you can always start"
          " dancing on your board like nobody's watching!")

    # Return both skill level and wind_sports list
    return skill_level, wind_sports


def is_suitable_wind_speed(skill_level, wind_speed):
    """Determines if the wind speed and gusts are
    suitable for windsurfing skill level.
    """
    time.sleep(5)
    print("\nLet's check if the current wind conditions suit your level!")
    print("\n...\n")
    time.sleep(3)

    beginner_max = 5  # Maximum wind speed: beginners (m/s)
    intermediate_max = 8  # Maximum wind speed: intermediate windsurfers (m/s)
    advanced_min = 12  # Minimum wind speed: advanced windsurfers (m/s)

    if skill_level == "Chill Surfer" and wind_speed > beginner_max:
        print(f"Hm... Wind speeds are a bit strong at {wind_speed} m/s for"
              f" beginners. Consider waiting for calmer conditions.")

    elif (skill_level in ("Freestyle Flyer", "Wave Slayer") and
          wind_speed > intermediate_max):
        print(f"Well, wind speeds might be challenging at {wind_speed} m/s"
              f" for {skill_level}s. Use caution or consider waiting.")

    elif (skill_level in ("Freestyle Flyer", "Wave Slayer") and
          wind_speed < intermediate_max):
        print(f"Well, wind speeds might be kinda slow at {wind_speed} m/s"
              f" for {skill_level}s. Enjoy anyway!")

    elif skill_level == "Legendary Windsurfer":
        pass  # No wind speed restriction for legendary windsurfers
        print(f"Apparently, you can conquer any wind and wave! Ride on!")
    else:
        print(f"Invalid skill level '{skill_level}'."
              f" Assuming beginner conditions.")
        if wind_speed > beginner_max:
            print(f"Wind speeds are a bit strong at {wind_speed} m/s"
                  f" for beginners. Consider waiting for calmer conditions.")

    return


def get_windsurfing_suitability(name, temperature, location):
    """Asks the user for water and air temperature preferences,
    offering guidance on windsurfing suitability based on their input.
    """
    time.sleep(5)
    print(f"\nNow, let's look a bit more at your preferences {name}!")
    while True:  # Get water preference with feedback
        preference = input(
            "\nHow do you prefer the water for windsurfing?"
            "'Warm' like a bath or 'cool' like a glacier?\n").lower()
        if preference in ("warm", "cool"):
            water_preference = preference
            if preference == 'warm':
                print(f"\nAh, a bathtub enthusiast! Perfect for"
                      f" practicing those mermaid impressions!")
            elif preference == 'cool':
                print(f"Excellent choice! Perfect for channeling"
                      f" your inner penguin (without the tuxedo).")
            else:
                print(f"\nHold on, {preference} water?"
                      f"Hey there, landlubber!")
                print(f" Those aren't water temperatures, but shower settings."
                      f" Try 'warm' or 'cool'.\n")
            break

    # Get air temperature tolerance and determine suitability
    time.sleep(3)
    print(f"\n Alright, {water_preference} water it is."
          f" Now, how do you handle air temperature?")
    tolerance = input(
        "Would you define yourself as a 'tropical lizard'"
        " or a 'polar bear'?\n").lower()

    ideal_min_temp = 18  # Minimum ideal air temperature (Celsius)
    ideal_max_temp = 28  # Maximum ideal air temperature (Celsius)

    if tolerance in ("tropical lizard", "polar bear"):
        if tolerance == 'tropical lizard':
            ideal_min = 22
            ideal_max = 32
        elif tolerance == 'polar bear':
            ideal_min = 12
            ideal_max = 22
    else:
        print(f"Those aren't the only options, but interesting choices!"
              f" We'll assume you're adaptable.")

    if temperature < ideal_min_temp:
        print(f"The air temperature in {location.split(',')[0].strip()}"
              f" is a bit chilly for windsurfing.")
        print("Consider wearing a wetsuit or layering up.")
    elif temperature > ideal_max_temp:
        print(f"The air temperature in {location.split(',')[0].strip()}"
              f" might be a bit hot.")
        print("Stay hydrated and consider sun protection.")
    else:
        print(f"The air temperature in {location.split(',')[0].strip()}"
              f" looks perfect for windsurfing!")

    time.sleep(3)
    return water_preference, temperature >= ideal_min


def get_weather_data(api_key, location):
    """Fetches weather data from Open Weather
    Map for the given location.
    """

    url = (
        f"https://api.openweathermap.org/data/2.5/"
        f"weather?q={location}&appid={api_key}&units=metric"
    )

    response = requests.get(url).json()  # json->to access specific attributes

    if response['cod'] == 200:  # Check if the request was successful
        # Extract and display relevant weather information here:

        weather = response['weather'][0]['main']
        temperature = response['main']['temp']
        feels_like = math.floor(response['main']['temp'])
        wind_speed = response['wind']['speed']
        print(f"Here come some quick current weather facts"
              f" for {location.split(',')[0].strip()}:")
        print(f"The weather is {weather}.")
        print(f"The temperature is {temperature}°C")
        print(f"It feels like {feels_like}°C.")
        print(f"The wind speed is {wind_speed} m/s \n")
        return weather, temperature, feels_like, wind_speed
    else:
        # Handle error: location not found, etc
        print(f"Error occurred while fetching weather data for {location}.")
        return None, None, None, None


def main():
    """ Run all program functions """

    name, location = welcome_user()  # Unpack name and location
    weather, _, temperature, wind_speed = get_weather_data(api_key, location)
    # Fetch weather data and discard unused values
    wind_sports = []  # Create an empty list for windsurf styles
    skill_level, _ = windsurfing_skill(name, wind_sports)  # Unpack skil level
    is_suitable_wind_speed(skill_level, wind_speed)  # call after skill level
    water_pref, is_suitable = get_windsurfing_suitability(
        name, temperature, location
    )  # Ask about water+air temp preferences. Determine windsurf. suitability

    time.sleep(2)
    print(f"\n{name}, here's a quick recap of how wind and water conditions"
          f" in {location.split(',')[0]} align with your preferences:")

    time.sleep(5)  # Delay for 5 secs before printing the summary
    print("\nWait a bit... The info is being wrapped up at any moment...")
    print("...")
    time.sleep(3)  # Delay for 3 seconds before printing the summary
    print(f"\nAllright {name}, let's wrap it up now!")
    print(f"Today in {location.split(',')[0].strip()},"
          f"the weather is {weather}.")
    time.sleep(1)
    print(f"The temperature is {temperature}°C.")
    time.sleep(1)
    print(f"The wind speed is {wind_speed} m/s; suitable for {skill_level}s")
    print(f"You might consider aiming for {wind_sports[0]}.")
    time.sleep(1)

    if is_suitable:
        print(f"The {water_pref} water temperature sounds perfect for you!")
        print("Looks like all conditions are lining up"
              " for a fantastic windsurfing day!")
    else:
        print(f"The air temperature might be a bit on the chilly side.")
        print("Consider wearing a wetsuit or layering up!")
    time.sleep(3)
    print("")
    print("")


wave_rider_ascii()
main()

print(f"That's it for now!")
print("We wish you a fantastic time conquering the waves")
print("")
print(r"""
          -.--.
          )  " '-,
          ',' 2  \_
           \q \ .  \
        _.--'  '----.__
       /  ._      _.__ \__
    _.'_.'  \_ .-._\_ '-, }
   (,/ _.---;-(  . \ \   ~
 ____ (  .___\_\  \/_/
(      '-._ \   \ |
 '._       ),> _) >
    '-._ c='  Cooo  -._
        '-._           '.
            '-._         `\
                '-._       '.
                    '-._     \
                        `~---'

""")
