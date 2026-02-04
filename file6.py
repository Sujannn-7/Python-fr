with open("log.txt", "r") as f:
    data = f.read()

if ("Python" in data):
    print(f"The word is at {data.find('Python')}th index")
else:
    print("Python is not present in the file. ")