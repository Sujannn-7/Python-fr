class Calculator:
    def __init__(self, number):
        self.number = number  
    
    @staticmethod
    def greet():
        print("Hello User")

    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    
    def square_root(self):
        if self.number<0:
            print("Square root is not defined for negative number.")
        else:
            print(f"The square root of {self.number} is {self.number**(1/2):.2f}")
    
num = int(input("Enter a number: "))
num = Calculator(num)
num.greet()
num.square()
num.cube()
num.square_root()
