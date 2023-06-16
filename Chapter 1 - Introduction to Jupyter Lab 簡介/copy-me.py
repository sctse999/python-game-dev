from random import *
answer = int(random() * 100 + 1)
guessed = False
guesses = 0
print("=== Guessing Game ===")
print("Guess a number from 1 to 100")
while not guessed:
    guess = int(input("Your guess: "))
    guesses += 1
    if guess == answer:
        guessed = True
        print(f"You got it in {guesses} guesses! The answer is {answer}")
    elif guess > answer:
        print("Too large! Try again!")
    else:
        print("Too small! Try again!")