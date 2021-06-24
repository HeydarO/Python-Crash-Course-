china = {
'first_name': 'chinara',
'last_name': 'orujova',
'age': '31',
'city': 'ashburn'
}

heydar = {
'first_name': 'heydar',
'last_name': 'orujov',
'age': '35',
'city': 'ashburn'
}

oruj = {
'first_name': 'oruj',
'last_name': 'orujov',
'age': '6',
'city': 'ashburn'
}

jasmine = {
'first_name': 'jasmine',
'last_name': 'orujova',
'age': '0.9',
'city': 'ashburn'
}

people = [china, heydar, oruj, jasmine]

for person in people:
    print(f"\nFirst name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age'].title()}")
    print(f"City: {person['city'].title()}")

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'].title())
print(person['city'].title())
