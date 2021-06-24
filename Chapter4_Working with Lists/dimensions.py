#Adding immutable list with tuple function
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


#Looping values in the Tuple:
for dimension in dimensions:
    print(dimension)

#Writing over a Tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
