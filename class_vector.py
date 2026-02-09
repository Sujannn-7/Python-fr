class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector in 2-d form is: ({self.i}i, {self.j}j)")

class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The vector in 3-d form is: ({self.i}i, {self.j}j, {self.k}k)")


i = int(input("Enter a number: "))
j = int(input("Enter a number: "))
k = int(input("Enter a number: "))
a = TwoDvector(i, j)
a.show()
b = ThreeDvector(i, j, k)
b.show()

