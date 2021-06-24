# Using if-elif-else function:
age = 65

if age < 4:
    print("Your admission cost is $0")
elif age > 4 and age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

#Simplifying the same code:
age = 65

if age < 4:
    price = 0
elif age > 4 and age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")

#Increasing number of elif functions:
age = 66

if age < 4:
    price = 0
elif age > 4 and age < 18:
    price = 25
elif age > 65:
    price = 20
else:
    price = 40

print(f"Your admission cost is ${price}")

#Omitting Else function at the end to make code more clearer:
age = 66

if age < 4:
    price = 0
elif age > 4 and age < 18:
    price = 25
elif age > 65:
    price = 20
elif age < 65:
    price = 40

print(f"Your admission cost is ${price}")
