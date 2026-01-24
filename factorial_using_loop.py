num = int(input("Enter any number: "))
i = 1
factorial = 1
while i<=num:
    factorial *= i
    i += 1
print(f"The factorial of {num} is {factorial}")


factorial_1 = 1
for i in range(1, num+1):
    factorial_1 *= i
print(factorial_1)
