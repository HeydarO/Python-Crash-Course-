"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.
"""

def read_files(filename):
    """Read the words in the files."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exists.")
        #pass
    else:
        print(contents)

prefix = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\'
filenames = [f"{prefix}dogs.txt", f"{prefix}cats.txt"]
for filename in filenames:
    read_files(filename)
