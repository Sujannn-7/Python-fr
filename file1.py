with open("sample_file.txt") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    print(line1, line2, line3)
    print(type(line1))