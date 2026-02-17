name = input("Enter your name: ")
address = input("Enter your address: ")
p_number = int(input("Enter your phone number: "))
detail = "Hello, I am {}. I am from {}. You can call me at {}"
detail = detail.format(name, address, p_number)
print(detail)
