import random

x = random.randint(1, 100)

guess = 0
i = 1

while guess != x:
    guess = int(input("Guess " + str(i) + ": "))

    if guess == x:
        print("Correct answer after", i, "guesses")
    elif guess < x:
        print("Clue: higher")
        i += 1
    elif guess > x:
        print("Clue: lower")
        i += 1

    if i == 10:
        print("you ran out of guesses, you lose!")
        exit()
