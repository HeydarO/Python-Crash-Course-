"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
"""
from random import choice

lucky_numbers = ['1','3','7','9','4','6','5','8','2','0','G','Y','Q','H']

lucky_number = choice(lucky_numbers)+choice(lucky_numbers)+choice(lucky_numbers)+choice(lucky_numbers)
print(f"Ticket matching with following numbers and letters wins $1 mln: {lucky_number}")
