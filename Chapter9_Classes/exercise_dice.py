"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint

### 6 sided dice
# tries = 1
# while tries <= 10:
#     dice = randint(1,6)
#     print(f"For the try #{tries}, the rolled dice come up with {dice}")
#     tries += 1

### 10 sided dice
# tries = 1
# while tries <= 10:
#     dice = randint(1,10)
#     print(f"For the try #{tries}, the rolled dice come up with {dice}")
#     tries += 1

### 20 sided dice
tries = 1
while tries <= 10:
    dice = randint(1,20)
    print(f"For the try #{tries}, the rolled dice come up with {dice}")
    tries += 1
