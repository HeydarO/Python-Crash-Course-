### Writing simple message to the file
filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. \n")
    file_object.write("I love creating apps that can run in a browser. \n")
