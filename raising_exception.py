a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b == 0:
    raise ZeroDivisionError(f"The number {a} is not divisible by 0")
else:
    print(f"{a} divided by {b} is: {a/b}")