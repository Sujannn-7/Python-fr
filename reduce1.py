from functools import reduce
l = [1, 2, 25, 201, 225, 146, 168, 200, 360, 361] 

def max(a, b):
    if (a>b):
        return a
    return b

greater = reduce(max, l)
print(f"The greatest number in the list is: {greater}")