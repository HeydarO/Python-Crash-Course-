my_pizzas = ['mazzarella', 'pepperonni', 'california']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Don Carleone')
friend_pizzas.append('Sausage')

print("My favority pizzas:")
for my_pizza in my_pizzas[:]:
    print(my_pizza)

print("\nMy friend's favority pizzas:")
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza)
