"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\programming_poll.txt'

while True:
    response = input("Why do you like programming?\n")
    if response == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{response}\n")
            print("If you want to exit this session simply type 'quit'.")
