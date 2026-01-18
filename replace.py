letter = """Dear <|name|>,

Congratulations, you are selected!
        
<|date|>
"""
name = input("Enter your name: ").title()
date = input("Enter today's date: ")
letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)
print(letter)