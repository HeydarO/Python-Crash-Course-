"""
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
"""

from random import choice

i = 0
my_lucky_number = '3G9H'

lucky_numbers = ['1','3','7','9','4','6','5','8','2','0','G','Y','Q','H']

while True:
    lucky_number = choice(lucky_numbers)+choice(lucky_numbers)+choice(lucky_numbers)+choice(lucky_numbers)
    # lucky_number = my_lucky_number
    if my_lucky_number == lucky_number:
        print(f"My ticket ({my_lucky_number}) come up after {i}")
        break
    else:
        i = i + 1
        print(f"{lucky_number} Not so lucky!")
