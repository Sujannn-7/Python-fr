l = [1, 2, 25, 201, 225, 146, 168, 200, 360]

def divisible_5(n):
    if (n % 5 == 0):
        return True
    return False

div_5 = filter(divisible_5, l)
print(list(div_5))
