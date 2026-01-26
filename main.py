#The game of Rock, Paper and Scissor:
import random
choices = ["r", "s", "p"]
computer = random.choice(choices)
your_input = input("""Enter:
'R' for Rock, 
'P' for Paper and
'S' for Scissors \n\t\t""").lower()
your_dict = {
    "r" : "Rock",
    "p" : "Paper",
    "s" : "Scissors"
}

if(your_input != "s" and your_input != "p" and your_input != "r"):
    print("Invalid Input!")


else:
    print(f"Computer Chose: {your_dict[computer]}")
    print(f"You Chose: {your_dict[your_input]}")


    if(computer == "r" and your_input == "p" ):
        print("You won!")

        
    elif (computer == "r" and your_input == "s"):
        print("You lost!")


    elif (computer == "r" and your_input == "r"):
        print("Draw!")


    elif (computer == "p" and your_input == "r"):
        print("You lost!")


    elif (computer == "p" and your_input == "s"):
        print("You won!")


    elif (computer == "p" and your_input == "p"):
        print("Draw!")


    elif (computer == "s" and your_input == "p"):
        print("You lost!")


    elif (computer == "s" and your_input == "r"):
        print("You won!")

    elif (computer == "s" and your_input == "s"):
        print("Draw!")



