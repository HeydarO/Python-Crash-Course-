age = input("How old are you? ")
age = int(age)

if age <= 3:
    print("\nYour movie ticket cost is free.")
elif age > 3 and age <= 12:
    print("\nYour movie ticket cost is $10.")
elif age > 12:
    print("\nYour movie ticket cost is $15.")
