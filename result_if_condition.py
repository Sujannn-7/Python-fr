percentage = float(input("Enter your percentage: "))
print(percentage)

if percentage >= 90:
    print("A+ -------> Outstanding")
elif percentage >= 80:
    print("A -------> Very Good")
elif percentage >= 70:
    print("B+ -------> Good")
elif percentage >= 60:
    print("B  -------> Above Average")
elif percentage >= 50:
    print("C -------> Average")
elif percentage >= 40:
    print("D -------> Pass ")
elif percentage < 40:
    print("F -------> Fail")
