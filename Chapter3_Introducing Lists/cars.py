# Organize a List permenantly with sort method
cars = ['bmw', 'audi', 'toyota','subaru']
cars.sort()
print(cars)

#Organize a list permenantly in reverse with sort method
cars.sort(reverse=True)
print(cars)

#Organize a list temporary with sorted method
cars = ['bmw', 'audi', 'toyota','subaru']

print("\nHere is the listing in original:")
print(cars)

print("\nHere is the listing sorted:")
print(sorted(cars))

print("\nHere is the listing in original again:")
print(cars)

#Organize a list in the reverse order with reverse() method
cars.reverse()
print(cars)

#Find the length of a list using len() function
n = len(cars)
print(n)
