from random import randint
n = randint(1, 100)
guesses = 0

while True:
    try:
        guesses += 1
        a = int(input("Enter your guess: "))
        if (a>n):
            print("Lower number, please!")
        elif (a<n):
            print("Higher number please!")
        else:
            print(f"You have guessed the number {n} in {guesses} attempts")
            break

    except ValueError:
        print("Please enter a valid guess. ")
