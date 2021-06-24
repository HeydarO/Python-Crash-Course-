"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""

from user_privileges import Privileges

user_privileges_1 = Privileges()
print(user_privileges_1.show_privileges())
