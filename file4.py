with open("donkey.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("######", "donkey")

with open("donkey.txt", "w") as f:
    f.write(new_data)