#Changing element with in a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#Replacing existing element in a list
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding additional element at the end of a list with append function
motorcycles.append('honda')
print(motorcycles)

#Adding element to a empty List by append function
motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting an element to a list with insert function
motorcycles.insert(1, 'ducati')
print(motorcycles)

#Removing an element from a List with remove function
del motorcycles[1]
print(motorcycles)

#Removing an element from a List with pop function
popped_element = motorcycles.pop(1)
print(motorcycles)
print(popped_element)

#Removing the last element from a List with pop function
the_last_element = motorcycles.pop()
print(f"My last motocycle was {the_last_element.title()}.")

#Removing an element by Value
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#Removing an element with an explanation
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
