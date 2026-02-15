try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(f"{a}/{b} = {a/b}")

except ZeroDivisionError:
    print("∞")
