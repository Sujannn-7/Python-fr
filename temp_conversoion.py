def temp():
    return (celsius*(9/5))+32
    

celsius = float(input("Enter your temperature in celsius: "))
fahrenheit = temp()
print(f"The temperature in fahrenheit is: {fahrenheit:.2f}")