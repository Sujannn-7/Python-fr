from try_finally import main
from arithmetic_menu import menu
n = int(input("""
    ===========Arithmetic Menu===========
    1. --------> Addition
    2. --------> Subtraction
    3. --------> Multiplication
    4. --------> Division
                        
    Select a choice: """))
print(menu(n))
