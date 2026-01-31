with open("twinkle_twinkle_little_star.txt", "r") as f:
    poem = f.read()
    word = input("Enter the word you want to find: ")
    if (word in poem):
        print(f"The word {word}  is present at {poem.find(word)}th index")
    else:
        print(f"The word {word} is not present in the poem")