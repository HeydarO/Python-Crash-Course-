#Printing a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accesing Elements in a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

#Capitalizing first letter of the word taken from the list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

#Printing the last items in a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

#Using individual values from a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was {bicycles[0].title()}."

print(message)

#Getting index error
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[5])
