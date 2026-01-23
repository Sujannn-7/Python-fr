num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the third number "))
num4 = int(input("Enter the fourth number "))


if(num1>num2 and num1>num3 and num1>num4):
    greatest = num1
elif(num2>num3 and num2>num4):
    greatest = num2
elif(num3>num4):
    greatest = num3
else:
    greatest = num4


if(num1<num2 and num1<num3 and num1<num4):
    smallest = num1
elif(num2<num3 and num2<num4):
    smallest = num2
elif(num3<num4):
    smallest = num3
else:
    smallest = num4


num = [num1, num2, num3, num4]
num.remove(greatest)
num.remove(smallest)


if(num[0]>num[1]):
    second_greatest = num[0]
    third_greatest = num[1]
else:
    second_greatest = num[1]
    third_greatest = num[0]

print(f"""
The greatest of {num1}, {num2}, {num3}, {num4} is: {greatest}\n
Second greatest is: {second_greatest}\n
Third greatest is: {third_greatest}\n
Smallest is: {smallest}
""")



