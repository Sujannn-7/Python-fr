class Teacher:
    name = "David"
    dept = "Science"
   
    def department(self):
        print(f"The name of teacher is {self.name} and the name of department is {self.dept}")

class Principal(Teacher):
    school_name = "SVS"
    def school(self):
        print(f"The name of school is {self.school_name}")

a = Principal()
a.department()
a.school()