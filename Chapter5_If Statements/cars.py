#Using if statement:
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Ignoring case in equality
car = 'Audi'
print(car == 'audi')

#Ignoring case in equality
car = 'Audi'
print(car.lower() == 'audi')
