sandwich_orders = ['pastrami', 'deli', 'phili','pastrami', 'herndon', 'laurel', 'pastrami']
finished_sandwiches = []
print("Deli has run out of Pastrami sandwich.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")

    finished_sandwiches.append(sandwich)

print(f"\n{finished_sandwiches}")
