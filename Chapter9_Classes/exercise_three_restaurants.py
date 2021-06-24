"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name}")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open now!")

my_restuarant = Restaurant('Don Capone', 'Italian')
oruj_restaurant = Restaurant('Menim Metbexim', 'Azerbaijani')
jasmine_restaurant = Restaurant('Moya Kuxna', 'Russian')
# print(f"{my_restuarant.restaurant_name} is next to the Ashburn Mall.")
# print(f"My restuarant is serving {my_restuarant.cuisine_type} cuisine.")

my_restuarant.describe_restaurant()
oruj_restaurant.describe_restaurant()
jasmine_restaurant.describe_restaurant()
