def conversion():
    return inches*2.54

inches = float(input("Enter your length in inches: "))
cm = conversion()
print(f"{inches} inch is: {cm} cm")