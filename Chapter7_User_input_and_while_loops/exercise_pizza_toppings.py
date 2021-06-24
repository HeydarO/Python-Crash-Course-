prompt = "\nPlease add your favority pizza toppings: "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(topping)
