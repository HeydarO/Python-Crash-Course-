travel = ['Dubai','Brussel','Copenhagen','Barcelona']
print("\nOriginal List:")
print(travel)

print("\nSorted the List Temporarily:")
print(sorted(travel))

print("\nOriginal List Again:")
print(travel)

print("\nSorted the List in reverse Temporarily:")
print(sorted(travel, reverse=True))

print("\nOriginal List Again:)")
print(travel)

print("\nReverse Original List:")
travel.reverse()
print(travel)

print("\nSort the List Permenantly:")
travel.sort()
print(travel)

print("\nSort the List in Reverse Permenantly:")
travel.sort(reverse=True)
print(travel)
