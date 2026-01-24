n = int(input("Enter any number: "))
for i in range(n,0,-1):
    print(" " * (n-i),end= "")
    print("*" * (2*i-1), end="")
    print()