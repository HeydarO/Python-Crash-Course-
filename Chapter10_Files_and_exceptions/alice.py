def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exists.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

prefix = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\'
filenames = [f"{prefix}alice.txt", f"{prefix}siddhartha.txt", f"{prefix}moby_dick.txt", f"{prefix}little_women.txt"]
for filename in filenames:
    count_words(filename)
