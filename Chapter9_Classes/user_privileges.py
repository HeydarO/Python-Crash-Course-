"""A set of classes related to user privileges"""

from user import User

class Privileges:
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
            self.privileges = privileges

    def show_privileges(self):
        print(f"Here is the privileges that admin user has: {self.privileges}.")

class Admin(User):
    def __init__(self, first_name, last_name, city, birth_date, login_attempts):
        super().__init__( first_name, last_name, city, birth_date, login_attempts)
        self.privileges = Privileges()
