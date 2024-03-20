# WAVERIDER

![WaveRider mockup](documentation/wr_mockup.png)

Visit the live deployed site: [WaveRider](https://wave-rider-fd4d233c3f5b.herokuapp.com/)

Return back to the [README.md](README.md) file.

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [PEP8 CI Validator](#validator)
  * [Lighthouse](#lighthouse)
  * [Responsiveness](#responsiveness)
  * [Browser Compatibility](#browser-compatibility)

* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

* [BUGS](#bugs)

- - -

## AUTOMATED TESTING

#### PEP8 CI Validator

[PEP8 CI Validator](https://pep8ci.herokuapp.com) was used to validate my run.py file.

File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI Validator](https://pep8ci.herokuapp.com)| ![screenshot](documentation/wr_validation_ci.png) | Passed. No warnings or errors |

- - -

#### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.
I tested only for Desktop results.

`Deployed Site`

| Site | Desktop | Notes |
| --- | --- | --- |
|[WaveRider](https://wave-rider-fd4d233c3f5b.herokuapp.com/) | ![screenshot](documentation/wr_validation_lighthouse.png) | Some minor warnings that I ignored. |

- - -

#### Responsiveness

I have not tested my deployed project on multiple devices to check for responsiveness issues.
The template is given by CI and I did not make any further changes apart from adding some padding round the terminal window.

- - -

#### Browser Compatibility

I have tested my deployed project on two different browsers to check for compatibility issues. I could not find any issues.

| Browser | Main page |
| --- | --- |
| Chrome | ![screenshot](documentation/wr_resp_browser_chrome.png) | 
| Edge | ![screenshot](documentation/wr_resp_browser_edge.png) | 

- - -

## MANUAL TESTING

#### Testing User Stories

`First Time Visitors`

| Goals | How are they achieved? |
| :--- | :--- |

| I want to see a captivating welcome message that showcases the game's purpose and excites me to play. | Achieved through the wave_rider_ascii function that displays an ASCII art logo and the welcome_user function that greets the user with styled text. |
| I want clear and concise instructions to guide me through the game's mechanics and features. | Achieved through structured and user-friendly prompts guiding the player. |
| I want the game to be visually appealing and easy to navigate through | Achieved through formatted text using the fontstyle library for greetings and prompts, making the text visually appealing. The code structure with clear function calls makes navigation easier. |

`Returning and Frequent Visitors`

|  Goals | How could they be achieved? |
| :--- | :--- |

| I want the game to remember my skill level and location from previous sessions for a more personalized experience. | Comments in the welcome_user function and windsurfing_skill function for future storage of this data. |
| I want to see new challenges or scenarios to keep the gameplay engaging and dynamic. | The game could be expanded to offer different challenges based on location or weather conditions. |
| I want the option to track my windsurfing progress and achievements within the game. | Similar to remembering user data, features for tracking progress and achievements. This would require additional functionalities like user accounts and databases. |

- - -

#### Full Testing

Full testing was performed on the following devices:

* DESKTOP-24171KO
* Display: Apple 27" LED Cinema

`Deployed Site`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail | Screenshot |
| --- | --- | --- | --- | --- | --- |


| ... | ... | ... | ... | ... | ... |

- - -

## BUGS

I haven't encountered any bugs that I'm aware of.