"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User:
    def __init__(self, first_name, last_name, city, birth_date, login_attempts):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.birth_date = birth_date
        self.login_attempts = login_attempts

    def describe_user(self):
        """Summary of the user info"""
        print(f"{self.first_name} was born in {self.city} in {self.birth_date}.")

    def greet_user(self):
        """Greeting of the user"""
        print(f"\nHi {self.first_name}, nice to see you here!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        print(f"You had {self.login_attempts} login attempts.")

    def reset_login_attempts(self):
        self.login_attempts = 0

# user_1 = User('Oruj', 'Orujov', 'Houston', '12/13/2014')
# user_2 = User('Jasmine', 'Orujova', 'Leesburg', '05/13/2020')
# user_3 = User('Heydar', 'Orujov', 'Moscow', '09/20/1985')
# user_4 = User('chinara','Orujova', 'Ganja', '09/08/1989')
#
# user_1.greet_user()
# user_1.describe_user()
#
# user_2.greet_user()
# user_2.describe_user()
#
# user_3.greet_user()
# user_3.describe_user()
#
# user_4.greet_user()
# user_4.describe_user()

user_1 = User('Heydar', 'Orujov', 'Moscow', '09/20/1985', 0 )

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

user_1.reset_login_attempts()
print(f"Reset your login attempts to {user_1.login_attempts}.")
