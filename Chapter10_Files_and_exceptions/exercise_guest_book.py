"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\guest_book.txt'

while True:
    guest = input("What is your name?\n")
    if guest == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{guest}\n")
            print(f"Welcome to the website, {guest}! If you want to exit registration of guest names type 'quit'.")
