# import json
#
# numbers = [2, 3, 5, 7, 11, 13]
#
# filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\numbers.json'
# with open(filename, 'w') as f:
#     json.dump(numbers, f)

import json

filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
