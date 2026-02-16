from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sum(a, b):
    return a+b

print(f"The sum of elements of the list 'l' is: {reduce(sum, l)}")