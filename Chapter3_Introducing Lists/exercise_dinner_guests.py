guests = ['Faraj','Tarik','Nijat','Murad','Vugar']
print(f"Hey {guests[0]}, I found bigger table for us, so I will invite 3 more people to joins us.")
print(f"Hey {guests[1]}, I found bigger table for us, so I will invite 3 more people to joins us.")
print(f"Hey {guests[2]}, I found bigger table for us, so I will invite 3 more people to joins us.")
print(f"Hey {guests[3]}, I found bigger table for us, so I will invite 3 more people to joins us.")
print(f"Hey {guests[4]}, I found bigger table for us, so I will invite 3 more people to joins us.")

guests.insert(0,'Baj')
guests.insert(3,'Hisham')
guests.insert(7,'Fran')

print(guests)

n = len(guests)
print(n)
