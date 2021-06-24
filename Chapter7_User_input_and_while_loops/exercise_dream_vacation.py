places = []


polling_active = True

while polling_active:
    place = input("\nIf you could visit one place in the world, where would you go? ")

    places.append(place)

    repeat = input("Would you like to add another place? (yes/ no) ")
    if repeat == "no":
        polling_active = False

# Polling is complete. Show the results.
print('\n--- Poll Results ---')
print("I would like to visit these places:")
for response in places:
    print(f"{response}")
