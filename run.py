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
    name = input("Hey there, windsurfer! What's your name? ")
    print(f"Welcome to WaveRider, {name}!\n")


welcome_user()