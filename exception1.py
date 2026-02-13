try:
    a = int(input("Enter a number: "))
    b = input("Enter something: ")
    print(f"sum = {a+b}")

except TypeError:
    print("Error: You cannot add a string and an integer")