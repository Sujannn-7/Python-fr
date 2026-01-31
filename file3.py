import random
def game():
    score = random.randint(1, 100)
    with open("high_score.txt") as f:
        high_score = f.read()
        if high_score != "":
            high_score = int(high_score)
        else:
            high_score = 0
    
    print(f"Your current score is: {score}")
    print(f"Your high score is: {high_score}")
    if score>high_score:
        with open("high_score.txt", "w") as f:
            f.write(str(score))
    return score

game()

