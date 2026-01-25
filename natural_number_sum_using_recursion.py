def sum_natural(n):
    if n == 0:
        return 0
    return n+sum_natural(n-1)

n = int(input("Enter a number: "))
sum = sum_natural(n)
print(f"The sum of first {n} natural number is: {sum}")