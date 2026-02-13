try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"Sum = {a+b}")
except ValueError:
    print("Invalid Input!")