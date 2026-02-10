class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"


a = int(input("Enter real part of first complex number: "))
b = int(input("Enter imaginary part of first complex number: "))
c = int(input("Enter real part of second complex number: "))
d = int(input("Enter imaginary part of second complex number: "))

c1 = Complex(a, b)
c2 = Complex(c, d)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
