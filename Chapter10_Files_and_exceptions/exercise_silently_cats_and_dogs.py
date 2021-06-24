"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""

def read_files(filename):
    """Read the words in the files."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exists.")
        pass
    else:
        print(contents)

prefix = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\'
filenames = [f"{prefix}dogs.txt", f"{prefix}cats.txt"]
for filename in filenames:
    read_files(filename)
