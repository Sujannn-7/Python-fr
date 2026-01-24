name = ["Tony", "Steve", "Bruce", "Thor", "Natasha", "Clint"]
for i in name:
    print(f"Good Morning {i}")
    if i.startswith("S"):
        print(f"Hello {i}")



print("\nUsing While Loop:")
i = 0
while i<len(name):
    print(f"Good Morning {name[i]}")
    i += 1
