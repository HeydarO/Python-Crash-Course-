#copying list to the another list:
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("May favorite foods are:")
for my_food in my_foods[:]:
    print(my_food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friends_foods[:]:
    print(friend_food.title())
