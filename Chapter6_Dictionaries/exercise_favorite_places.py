china = {
'first place': 'Italy',
'second place': 'Tailand',
'third place': 'Budapest',
}

heydar = {
'first place': 'Swizerland',
'second place': 'Saint Peterburg',
'third place': 'Greece',
}

favorite_places = [china, heydar]

for visit in favorite_places:
    print(f"\nFirst place to visit is {visit['first place']}")
    print(f"Second place to visit is {visit['second place']}")
    print(f"Third place to visit is {visit['third place']}")
