favority_number = {
'chinara': '5',
'oruj': '12',
'jasmine': '12',
'maleyka': '100',
'gulshan': '1000',
}

#print("Checking if set function works:")
#for number in set(favority_number.values()):
#    print(number.title())

print(favority_number['chinara'])
print(favority_number['oruj'])
print(favority_number['jasmine'])
print(favority_number['maleyka'])
print(favority_number['gulshan'])

### Adding each name to the separate link with the number they like:
people = {
    'chinara': {
        'first_number': '5',
        'second_number': '10',
    },
    'oruj': {
        'first_number': '12',
        'second_number': '50',
    },

    'jasmine': {
        'first_number': '12',
        'second_number': '100',
    },

    'maleyka': {
        'first_number': '1',
        'second_number': '5',
    },

    'gulshan': {
        'first_number': '1000',
        'second_number': '1000000',
    },
}

for name, number in people.items():
    print(f"{name}'s favority number is {number['first_number']}")
    print(f"{name}'s favority number is {number['second_number']}")
