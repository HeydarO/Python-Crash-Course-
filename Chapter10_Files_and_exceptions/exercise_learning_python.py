"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.
"""
### Writing a list of strings 3 times using loops
file_path = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\learning_python.txt'

i = 1
while i<=3:
    with open(file_path) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
    i+=1

### Writing a list of strings 3 times using stored blocks
file_path = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\learning_python.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    print(line.rstrip())
    print(line.rstrip())
