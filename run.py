# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import requests
import time
import math
import random
import pyfiglet
import fontstyle
import os

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
    text_w_u_01 = fontstyle.apply("Welcome to WaveRider, your digital"
                                  " windsurfing companion!",
                                  'bold/italic/yellow/cyan_bg')
    print(text_w_u_01)
    print("")
    print("Hey there, windsurfer! Hope you are you ready "
          "to conquer the waves today!")
    print("")

    while True:
        try:
            name = input("What's your name, Captain?\n").upper()
            if not name.isalpha():
                raise ValueError("Whoa there, sailor!"
                                 " Names can only have letters (a-z).\n")
            while True:
                location = input(f"Ahoy,{name}! Where are you anchored"
                                 f" today? (e.g., City, Country)\n").upper()
                try:
                    city, country = location.strip().split(",")
                    city = city.strip()
                    country = country.strip()
                    if not city or not country:
                        raise ValueError("Well matey, you need to enter"
                                         " both city and country separated"
                                         " by a comma.\n")
                    # Enter API endpoint URL to validate city
                    url = (
                        f"https://api.openweathermap.org/data/2.5/"
                        f"weather?q={location}&appid={api_key}&units=metric"
                    )
                    response = requests.get(url).json()

                    # Check if the API response indicates a valid city
                    if response['cod'] == 200:
                        city_name = city  # Extract city name into a variable
                        # Show only the city in the welcome message
                        print(f"Splendid! {city_name} is "
                              f"such a beautiful place!\n")
                        time.sleep(1)
                        fetch_info = fontstyle.apply(f"Let me fetch you a bit"
                                                     f" of info about"
                                                     f" {city_name}!",
                                                     'bold/cyan')
                        print(fetch_info)
                        break
                    else:
                        print(f"Hmm, we couldn't find that location. "
                              "Maybe you misspelled something? "
                              "Try again and don't forget the ',' "
                              "between city and country!")
                except ValueError as err:
                    print("Did you mean something like 'Los Angeles, US'?"
                          " (Enter: city, country)")

            break

        except ValueError as err:
            print(f'{err}Maybe the rum got the better of you? Try again.')

    time.sleep(1)
    return name, location  # Return the location variable along with name


def windsurfing_skill(name, wind_sports):
    """Asks the user for their windsurfing skill level."""
    time.sleep(4)
    text_03 = fontstyle.apply(f"\nNow, let's get to know you "
                              f"better {name}", 'bold/cyan')
    print(text_03)

    print(f"On a scale of 1 to 10, how would you"
          f" rate your windsurfing skills?")
    print(f" 1: chill surfer and 10: gnarly surfer")
    print(f" p.s The sky is the limit; so greater numbers apply too!")
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
              f" Are you whispering to the wind gods?")
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
    text_04 = fontstyle.apply(f"\nLet's check if the current wind conditions "
                              f"suit your level!", 'bold/cyan')
    print(text_04)
    time.sleep(3)
    print("...")
    time.sleep(2)
    print("Almost there...")
    time.sleep(1)

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
    text_05 = fontstyle.apply(f"\nNow, let's look a bit more at your"
                              f" preferences {name}!", 'bold/cyan')
    print(text_05)
    while True:  # Get water preference with feedback
        preference = input(
            "How do you prefer the water for windsurfing?"
            "'Warm' like a bath or 'cool' like a glacier?\n").lower()
        if preference in ("warm", "cool"):
            water_preference = preference
            if preference == 'warm':
                print(f"Ah, a bathtub enthusiast! Perfect for"
                      f" practicing those mermaid impressions!")
            elif preference == 'cool':
                print(f"Excellent choice! Perfect for channeling"
                      f" your inner penguin (without the tuxedo).")
            else:
                print(f"Hold on, {preference} water?"
                      f"Hey there, landlubber!")
                print(f" Those aren't water temperatures, but shower settings."
                      f" Try 'warm' or 'cool'.")
            break

    # Get air temperature tolerance and determine suitability
    time.sleep(3)
    print(f"Alright, {water_preference} water it is.")

    text_06 = fontstyle.apply(f"\nNow, how do you handle air"
                              f" temperature?", 'bold/cyan')
    print(text_06)
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
              f" is a bit chilly for windsurfing."
              f" Yes... Even for a {tolerance} of your kind.")
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
        print(f"1.The weather is: {weather}.")
        time.sleep(1)
        print(f"2.The temperature is: {temperature}°C")
        time.sleep(1)
        print(f"3.It feels like {feels_like}°C.")
        time.sleep(1)
        print(f"4.The wind speed is {wind_speed} m/s")
        time.sleep(1)
        return weather, temperature, feels_like, wind_speed
    else:
        # Handle error: location not found, etc
        print(f"Error occurred while fetching weather data for {location}.")
        return None, None, None, None


def centered_statement(statement, terminal_width=75):
    """Print a centered statement between each step of the code.
    It is integrated in main, between the various steps of the code unlocking.
    """
    # Calc number of spaces needed to center the statement
    spaces = (terminal_width - len(statement)) // 2
    # Construct centered statement
    centered_statement_print = " " * spaces + statement

    print(centered_statement_print)


def main():
    """ Run all program functions """

    name, location = welcome_user()  # Unpack name and location
    print("")
    time.sleep(1)
    weather, _, temperature, wind_speed = get_weather_data(api_key, location)
    # Fetch weather data and discard unused values
    wind_sports = []  # Create an empty list for windsurf styles
    skill_level, _ = windsurfing_skill(name, wind_sports)  # Unpack skil level
    print("")
    centered_statement("-****--****--****--****-", 75)
    print("")
    time.sleep(1)
    is_suitable_wind_speed(skill_level, wind_speed)  # call after skill level
    water_pref, is_suitable = get_windsurfing_suitability(
        name, temperature, location
    )  # Ask about water+air temp preferences. Determine windsurf. suitability
    print("")
    centered_statement("-****--****--****--****-", 75)
    print("")

    time.sleep(2)
    text_final = fontstyle.apply(f"{name}, here's a quick recap of how wind"
                                 f" and water conditions in"
                                 f" {location.split(',')[0]}"
                                 f" align with your preferences:",
                                 'bold/italic/yellow/cyan_bg')
    print(text_final)
    print("")
    time.sleep(5)  # Delay for 5 secs before printing the summary
    print("Wait a bit... The info is being wrapped up at any moment...")
    print("...")
    time.sleep(3)  # Delay for 3 seconds before printing the summary
    print(f"Allright {name}, let's wrap it up now!")
    print(f"1.Today in {location.split(',')[0].strip()},"
          f"the weather is {weather}.")
    time.sleep(1)
    print(f"2.The temperature is {temperature}°C.")
    time.sleep(1)
    print(f"3.The wind speed is {wind_speed} m/s; suitable for {skill_level}s")
    print(f"4.You might consider aiming for {wind_sports[0]}.")
    time.sleep(1)

    if is_suitable:
        print(f"5.The {water_pref} water temperature sounds perfect for you!")
        print("Looks like all conditions are lining up"
              " for a fantastic windsurfing day!")
    else:
        print(f"5.The air temperature might be a bit on the chilly side.")
        print("Consider wearing a wetsuit or layering up!")
    time.sleep(3)
    print("")
    print("")


def ending_text():
    """Conclusion text
    """
    time.sleep(5)
    print(f"That's it for now!")
    print("We wish you a fantastic time conquering the waves!")
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
       '-._ cooo cooo  -._
            '-._           '.
                '-._         `\
                '-._       '.
                        '-._     \
                            `~---'


    """)


wave_rider_ascii()
main()
time.sleep(2)
ending_text()
