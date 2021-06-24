"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""

import json

def get_stored_number():
    """Get stored username's favorite number"""
    filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    """Prompt for a new favority number."""
    number = input("What is your favorite number? ")
    filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
        return number

def check_number():
    """Check if user entered his favorite number."""
    number = get_stored_number()
    if number:
        print(f"Your favority number is {number}!")
    else:
        username = get_new_number()
        print(f"We know your favority number now, hehe!")

check_number()
