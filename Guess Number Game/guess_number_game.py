import random

number = random.randrange(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess > number:
        print("You guessed a higher number. \n")
        guess = int(input("Guess a number between 1 and 100: "))
    elif guess < number:
        print("You guessed a lower number. \n")
        guess = int(input("Guess a number between 1 and 100: "))
print("You did it!")
