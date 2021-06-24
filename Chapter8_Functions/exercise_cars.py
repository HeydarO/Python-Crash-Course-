"""
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""

def car_details(manufacturer, model_name, **other_info):
    """Build a dictionary containing everything we know about a car."""
    other_info['manufacturer'] = manufacturer
    other_info['model_name'] = model_name
    return other_info

car_details = car_details('toyota', 'LE Plus',
                            color = 'grey',
                            Four_wheel = False)
print(car_details)
