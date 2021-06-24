# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
#
# make_pizza('pepperoni')
# make_pizza('mushroom', 'green peppers', 'extra cheese')

# ### Separating toppings based on number of requests
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMake a pizza with the following toppings:")
#     for topping in toppings:
#         print(f" - {topping}")
#
# make_pizza('pepperoni')
# make_pizza('mushroom', 'green peppers', 'extra cheese')

### Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMake a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
