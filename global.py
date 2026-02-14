a = 112
def num():
    a = 12
    print(a)

print(a)
num()


b = 27
def num1():
    global b
    b = 16
    print(b)

num1()
print(b)


