"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\guest.txt'

guest = input("Welcome to the website, what is your name?\n")

with open(filename, 'a') as file_object:
    file_object.write(f"{guest}\n")
