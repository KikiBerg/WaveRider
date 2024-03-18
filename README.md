# WAVERIDER

![WaveRider mockup](documentation/wr_mockup.png)

Visit the live deployed site: [WaveRider](https://wave-rider-fd4d233c3f5b.herokuapp.com/)

This project is my third student project.

## ABOUT WAVERIDER

"Wave Rider" offers a fun journey into the world of windsurfing, providing a personalized experience that caters to users' unique preferences and skills. The game dynamically adjusts to the users' skill level, ensuring an engaging adventure for all.
Read more about the game in the [Features](README.md) section.

## CONTENTS

* [User Experience](#user-experience-ux)

* [User Stories](#user-stories)

* [Features](#features)  
  * [Existing Features](#features)
  * [Future Implementations](#future-implementations) 

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

- - -

## User Experience (UX)

I wanted to create a game that is engaging, informative, and user-friendly.
I wanted the game to help windsurfing enthusiasts of all skill levels and provide a personalized and engaging experience from start to finish.

* Welcome and Introduction:
Upon starting the game, users are greeted with a warm welcome message and an eye-catching ASCII art title ("Wave Rider"), setting the tone for an exciting windsurfing adventure.

* Personalization:
The game begins by prompting users to enter their name and location, allowing for a personalized experience. User inputs are validated to ensure correctness.

* Interactive Dialogue:
Users engage in interactive dialogue throughout the game, responding to prompts and making choices regarding their windsurfing skill level, temperature preferences, and more.

* Feedback and Guidance:
The game provides feedback and guidance tailored to the user's inputs. For example, users receive encouragement based on their chosen skill level and recommendations regarding wind and temperature suitability for windsurfing.

* Visual Presentation:
Visual elements such as ASCII art and centered statement printing enhance the visual appeal of the game, making it visually engaging and easy to follow.

* Information Accessibility:
Important information such as weather data and user preferences are presented clearly and succinctly, ensuring easy comprehension and accessibility.

* Progressive Disclosure:
The game unfolds gradually, revealing information and options in a progressive manner. Users are guided step-by-step through the windsurfing assessment process, preventing information overload.

* Conclusion and Well Wishes:
The game concludes with a positive message, wishing users a fantastic time conquering the waves. This conclusion leaves users with a sense of satisfaction and anticipation for their windsurfing adventure.

- - -

## User Stories

#### First Time Visitor Goals

* As a first-time visitor, I want to see a captivating welcome message that showcases the game's purpose and excites me to play.
* As a first-time visitor, I want clear and concise instructions to guide me through the game's mechanics and features.
* As a first-time visitor, I want the game to be visually appealing and easy to navigate through.

#### Returning and frequent Visitor Goals

* As a returning visitor, I want the game to remember my skill level and location from previous sessions for a more personalized experience.
* As a returning visitor, I want to see new challenges or scenarios to keep the gameplay engaging and dynamic.
* As a frequent visitor, I want the option to track my windsurfing progress and achievements within the game.

- - -

## Features

#### Existing Features

Τhe game simulates a conversation between a windsurfer and a digital companion named Wave Rider. 
Here are the existing features:

* Welcome message and user input:
    * The program welcomes the user and asks for their name and location.
    * It validates the user's input to ensure it consists only of letters (for name) and separates city and country with a comma (for location).

* Skill level determination:
    * The program asks the user about their windsurfing skill level on a scale of 1 to 10.
    * Based on the user's input, it categorizes them as a "Chill Surfer," "Freestyle Flyer," "Wave Slayer," or "Legendary Windsurfer."
    * It also suggests windsurfing styles (cruising, freestyle maneuvers, catching waves) suitable for their skill level.

* Weather data retrieval:
    * The program uses an API key to fetch weather data (weather type, temperature, wind speed) for the user's location from [Open Weather Map](https://openweathermap.org/)

* Suitability assessment:
    * The program asks the user about their water temperature preference and air temperature tolerance.
    * It compares the user's preferences with the retrieved weather data to determine if the conditions are suitable for windsurfing.

* Summary and recommendations:
    * The program summarizes the user's preferences, windsurfing skill level, and weather data.
    * It provides recommendations on windsurfing styles (based on skill level) and suggests if a wetsuit might be necessary (based on air temperature).

* Ending message:
    * The program concludes the interaction with a goodbye message and encourages the user to enjoy their windsurfing experience.


#### Future Implementations