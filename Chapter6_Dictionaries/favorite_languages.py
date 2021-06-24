favorite_languages = {
'jen': 'Python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['jen', 'collins', 'taylor', 'edward', 'phil', 'natasha', 'peter']

for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking time to respond!")
    else:
        print(f"{name.title()}, we will really appreciate if you take this poll.")


### Using set() function - DID NOT WORK FOR SOME REASON
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

### Using values() function
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

### Using keys() function
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

###
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

### Using loop and if statement with dictionaries
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

###
for name in favorite_languages:
    print(name.title())

###
for name in favorite_languages.keys():
    print(name.title())

###
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favority language is {language.title()}.")

###
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

###
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite language is {languages[0].title()}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
