n = int(input("Enter a number: "))
tables = [str(n*i) for i in range(1, 11)]
s = "\n".join(tables)
print(s)
