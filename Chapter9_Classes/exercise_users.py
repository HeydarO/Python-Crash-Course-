"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""
class User:
    def __init__(self, first_name, last_name, city, birth_date):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.birth_date = birth_date

    def describe_user(self):
        """Summary of the user info"""
        print(f"{self.first_name} was born in {self.city} in {self.birth_date}.")

    def greet_user(self):
        """Greeting of the user"""
        print(f"\nHi {self.first_name}, nice to see you here!")

user_1 = User('Oruj', 'Orujov', 'Houston', '12/13/2014')
user_2 = User('Jasmine', 'Orujova', 'Leesburg', '05/13/2020')
user_3 = User('Heydar', 'Orujov', 'Moscow', '09/20/1985')
user_4 = User('chinara','Orujova', 'Ganja', '09/08/1989')

user_1.greet_user()
user_1.describe_user()

user_2.greet_user()
user_2.describe_user()

user_3.greet_user()
user_3.describe_user()

user_4.greet_user()
user_4.describe_user()
