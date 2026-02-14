def menu(n):
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    match n:
        case 1:
            return f"The sum is: {a+b}" 
        case 2:
            return f"The difference is:{a-b}"
        case 3:
            return f"The product is: {a*b}"
        case 4:
            if b!=0:
                return f"The quotient is: {a//b}"
            else:
                return "Division by Zero is not Possible"
        case _:
            return "Please, enter a number from 1-4"



    n = int(input("""
    ===========Arithmetic Menu===========
    1. --------> Addition
    2. --------> Subtraction
    3. --------> Multiplication
    4. --------> Division
                        
    Select a choice: """))
    print(menu(n))
