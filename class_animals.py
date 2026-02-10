class Animals:
    def show(self):
        print("The Animal is a living thing.")

class Pets(Animals):
    def show(self):
        print("The pets are domisticated animals. ")

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Bow bow ")

a = Dogs()
a.bark()
a.show()