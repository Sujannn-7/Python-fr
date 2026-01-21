list = []
fruit1 = input("Enter first fruit ")
fruit2 = input("Enter second fruit ")
fruit3 = input("Enter third fruit ")
fruit4 = input("Enter fourth fruit ")
fruit5 = input("Enter fifth fruit ")
list.append(fruit1)
list.append(fruit2)
list.append(fruit3)
list.append(fruit4)
list.append(fruit5)
print(list)


list = []
i= 1
while i<=5:
    fruit = input("Enter a fruit name ")
    fruit = fruit.capitalize()
    list.append(fruit)
    i += 1

print(list)