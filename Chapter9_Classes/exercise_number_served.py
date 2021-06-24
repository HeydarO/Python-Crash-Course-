"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
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

my_restuarant = Restaurant('Don Capone', 'Italian')
print(f"{my_restuarant.restaurant_name} is next to the Ashburn Mall.")
print(f"My restuarant is serving {my_restuarant.cuisine_type} cuisine.")
# print(f"We've served {my_restuarant.number_served} customers today.")

# my_restuarant.number_served = 20
# print(f"We've served {my_restuarant.number_served} customers today.")

my_restuarant.describe_restaurant()
my_restuarant.open_restaurant()
my_restuarant.set_number_served(20)
my_restuarant.increment_number_served(10)
