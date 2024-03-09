# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import requests
from tkinter import *
import math
import random

api_key = "e33690fb74cac3d02cc1384e38f73c7d"

def welcome_user():
    """Greets the user welcome and asks for their name."""
    print("Welcome to WaveRider! Your ultimate companion for conquering the windswept waves with finesse and confidence.\n")
    while True:
        name = input("Hey there, windsurfer! What's your name? ")

        try:
            if name.isalpha():                
                print(f"Welcome to WaveRider, {name}!\n")
                break
            elif len(name) == 0:
                print("Why not provide a name?")
            else:
                print(f"{name} is invalid. You can only enter letters a-z\n")
        except ValueError as err:
            print(f'{err}. Please try again.')           



welcome_user()