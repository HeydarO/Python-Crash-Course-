### Printing file contents
file_path = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

### Printing each line within the file one by contents
file_path = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\pi_digits.txt'

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

### Retaining contents of the file within the list and printing it outside of WITH function
file_path = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
        print(line.rstrip())
