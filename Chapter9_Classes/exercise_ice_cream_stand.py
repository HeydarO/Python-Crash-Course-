"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"\n{self.restaurant_name}")
        print(f"{self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open now!")

    def set_number_served(self, number_served):
        """Set number of customers served"""
        self.number_served = number_served
        print(f"We've served {self.number_served} customers today.")

    def increment_number_served(self, meals):
        """Increment the number of customers who’ve been served"""
        self.meals = meals
        print(f"We usually serve {self.meals} meals per day.")

    def flavors(self):
        self.flavors = 'sweet', 'sour', 'bitter', 'salty', 'umami (savory)'
        print(f"We have following flavors in our restaurant: {self.flavors}.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """"
        Initialize attributes of the parent class
        Then initialize attributes specific to the IceCreamStand class
        """
        super().__init__(restaurant_name, cuisine_type)


my_restuarant = IceCreamStand('Don Capone', 'Italian')
my_restuarant.flavors()
# print(f"{my_restuarant.restaurant_name} is next to the Ashburn Mall.")
# print(f"My restuarant is serving {my_restuarant.cuisine_type} cuisine.")

# my_restuarant.describe_restaurant()
# my_restuarant.open_restaurant()
# my_restuarant.set_number_served(20)
# my_restuarant.increment_number_served(10)
