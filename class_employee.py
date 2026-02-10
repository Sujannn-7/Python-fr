class Employee:
    def __init__(self, salary):
        self.salary = salary
        print(f"The salary is: {self.salary}")


    def increment(self, increase):
        self.increase = increase
        self.salary += increase
        print(f"Your incremented salary is:{self.salary} ")
        
        

salary = int(input("Enter your employee's salary: "))
increase = int(input("Enter your employee's increment: "))
a = Employee(salary)
a.increment(increase)
