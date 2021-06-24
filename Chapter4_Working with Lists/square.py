#finding square of the each number between 1 and 10 using list() and range() functions
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

#improving code and get the same result as above:
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

#improving code even more using list comprehensions and getting the same results:
squares = [value ** 2 for value in range(1,11)]
print(squares)

#simple math operations with Python:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
