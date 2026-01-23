spam_messages = {"YOU WON A IPHONE 11","YOU WON THE LOTTERY"}
message = input("Enter a message ")
message = message.upper()
if message in spam_messages:
    print("This looks like a spam message.")
else:
    print("Thank you for sending a message. ")