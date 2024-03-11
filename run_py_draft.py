def get_windsurfing_suitability():
  """Asks the user for water and air temperature preferences,
  offering guidance on windsurfing suitability based on their input.

  Returns:
    tuple: A tuple containing the user's water preference (str)
           and air temperature suitability (bool).
  """

  # Get water preference with feedback
  while True:
    preference = input("Do you prefer the water warm (like a bath) or cool (like a glacier) for windsurfing? ").lower()
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

  ideal_min = 18  # Minimum ideal air temperature (Celsius)
  ideal_max = 28  # Maximum ideal air temperature (Celsius)

  if tolerance in ("tropical lizard", "polar bear"):
    # Adjust ideal range based on tolerance (optional)
    if tolerance == "tropical lizard":
      ideal_min = 22
      ideal_max = 32
    elif tolerance == "polar bear":
      ideal_min = 12
      ideal_max = 22
  else:
    print(f"Those aren't the only options {name}, but interesting choices! We'll assume you're adaptable.")

  temperature = float(input("Enter the current air temperature (in Celsius): "))

  if temperature < ideal_min:
    print("The air temperature is a bit chilly for windsurfing. Consider wearing a wetsuit or layering up.")
  elif temperature > ideal_max:
    print("The air temperature might be a bit hot. Stay hydrated and consider sun protection.")
  else:
    print("The air temperature looks perfect for windsurfing!")

  return water_preference, temperature >= ideal_min  # Suitable if minimum threshold is met

# Example usage
water_pref, is_suitable = get_windsurfing_suitability()
print(f"\nWindsurfing suitability based on your preferences:")
print(f"  Water preference: {water_pref}")
print(f"  Air temperature suitable: {is_suitable}")




######################


def main():
    """ Run all program functions """
    name = welcome_user()
    wind_sports = []
    skill_level, wind_sports = windsurfing_skill(name, wind_sports)  # Pass the empty list

    # Get water and temperature tolerance after getting windsurfing skill
    water_preference, tolerance = get_water_and_temperature_tolerance()

    # Now you have all the information: name, skill level, wind sports, water preference, and temperature tolerance
    # Use this information to provide recommendations or suggestions to the user

    print(f"\nGreat to know your preferences, {name}! As a {skill_level}, {wind_sports[0]} sounds like a fun activity.")

    # Example: Conditionally suggest based on water preference and temperature tolerance
    if water_preference == "warm" and tolerance == "tropical lizard":
        print(f"Since you prefer warm water and enjoy the heat, you might enjoy locations with calmer waters and consistent sunshine.")
    elif water_preference == "cool" and tolerance == "polar bear":
        print(f"You prefer cool water and can handle cooler temperatures? Look for locations with waves and potentially windier conditions.")
    else:
        print(f"With your adaptability to water temperature and air temperature, you have a wider range of options to explore!")

    # You can further enhance this section with logic based on weather data or external resources

    print("\nWe hope WaveRider helped you plan your windsurfing adventure! Stay safe and have fun out there!")

main()



def is_suitable_air_temperature(temperature):
    """Determines if the air temperature is suitable for windsurfing.

    Args:
        temperature (float): The air temperature in degrees Celsius.

    Returns:
        bool: True if the temperature is suitable, False otherwise.
    """

    ideal_min = 18  # Minimum ideal air temperature (Celsius)
    ideal_max = 28  # Maximum ideal air temperature (Celsius)

    if temperature < ideal_min:
        print("The air temperature is a bit chilly for windsurfing. Consider wearing a wetsuit or layering up.")
    elif temperature > ideal_max:
        print("The air temperature might be a bit hot. Stay hydrated and consider sun protection.")
    else:
        print("The air temperature looks perfect for windsurfing!")

    return temperature >= ideal_min  # Suitable if minimum threshold is met

def is_suitable_wind_speed(wind_speed, wind_gust):
    """Determines if the wind speed and gusts are suitable for windsurfing skill level.

    Args:
        wind_speed (float): The average wind speed in meters per second.
        wind_gust (float): The maximum wind gust speed in meters per second.

    Returns:
        bool: True if the wind conditions are suitable, False otherwise.
    """

    beginner_max = 7  # Maximum wind speed for beginners (m/s)
    intermediate_max = 10  # Maximum wind speed for intermediate windsurfers (m/s)
    advanced_min = 12  # Minimum wind speed for advanced windsurfers (m/s)

    print("What is your windsurfing skill level?")
    skill_level = input("(Enter 'beginner', 'intermediate', or 'advanced'): ").lower()

    if skill_level == "beginner":
        if wind_speed > beginner_max:
            print(f"Wind speeds are a bit strong at {wind_speed:.1f} m/s for beginners. Consider waiting for calmer conditions.")
            return False
    elif skill_level == "intermediate":
        if wind_speed > intermediate_max:
            print(f"Wind speeds might be challenging at {wind_speed:.1f} m/s for intermediate windsurfers. Use caution or consider waiting.")
            return False
    elif skill_level == "advanced":
        if wind_speed < advanced_min:
            print(f"Wind speeds might be too light at {wind_speed:.1f} m/s for advanced windsurfers. Consider waiting for stronger winds.")
            return False
    else:
        print(f"Invalid skill level '{skill_level}'. Assuming beginner conditions.")
        if wind_speed > beginner_max:
            print(f"Wind speeds are a bit strong at {wind_speed:.1f} m/s for beginners. Consider waiting for calmer conditions.")
            return False

    # Wind conditions are suitable if we haven't returned False yet
    return True




    def main():
    """Prompts user for location, fetches weather data, and provides recommendations."""

    location = input("Enter the location (city, state, etc.): ")
    weather_data = get_weather_data(location)

    if weather_data is not None:
        try:
            air_temp = weather_data["main"]["temp"]
            wind_speed = weather_data["wind"]["speed"]
            wind_gust = weather_data.get("wind", {}).get("gust", None)  # Handle optional