#Using inequality in the code with if statement:
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms'in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni'in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#Using inequality in the code with elif function:
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms'in requested_topping:
    print("Adding mushrooms.")
elif 'pepperoni'in requested_topping:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#Using loop with lists:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#Using loop with lists, example of not available topping:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers now.')
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#Working with empty lists:
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print('Are you sure you want plain pizza?')

#Using Multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFnished making your pizza!")
