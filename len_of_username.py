username = input("Enter yourusername ")
print(len(username))
if len(username)>50:
    print("Your username should consist characters less than 50.")
elif len(username)<=0: 
    print("Your username should consist at least 1 character.")
else:
    print("Thank you for entering your username.")
