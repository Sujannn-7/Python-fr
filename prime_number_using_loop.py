n = int(input("Enter any number: "))

for i in range(2,n):
    if n%i == 0:
        print("The number is not prime. ")
        break
    else:
        print("The number is prime")