"""Number Guessing Game."""
from random import randint
from numpy import append
x: int = 3
correct: bool = False

while correct == False:
    secret: int = randint(1,x)
    guess: int = int(input('Guess a number: '))
    if guess == secret:
        print(f"Correct! {guess} is the number")
        correct = True
    elif guess > secret:
        print("Guess is too high!")
        x += 1
    else:
        print("Guess is too low!")
        x += 1




