sandwich_orders = ['deli', 'phili', 'herndon', 'laurel']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")

    finished_sandwiches.append(sandwich)

print(f"\n{finished_sandwiches}")
