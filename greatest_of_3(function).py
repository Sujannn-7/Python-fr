def greatest():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the first number: "))
    c = int(input("Enter the first number: "))

    if a>b and a>b:
        greatest = a
    elif b>c:
        greatest = b
    else:
        greatest = c
    print(f"The greatest of {a}, {b} and {c} is: {greatest}")
    
greatest()
