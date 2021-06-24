"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name}")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open now!")

my_restuarant = Restaurant('Don Capone', 'Italian')
print(f"{my_restuarant.restaurant_name} is next to the Ashburn Mall.")
print(f"My restuarant is serving {my_restuarant.cuisine_type} cuisine.")

my_restuarant.describe_restaurant()
my_restuarant.open_restaurant()
