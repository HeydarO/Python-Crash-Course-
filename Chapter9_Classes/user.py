"""A class that is represent users"""

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
