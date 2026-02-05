class Employee:
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language


sujan = Employee("Sujan", "130000", "Python")
print(f"{sujan.name}\n{sujan.salary}\n{sujan.language}\n")