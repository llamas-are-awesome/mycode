#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)
    i = 1
    while i <= 5 :
        try:

            print(f"Guess {i} of 5")
            guess= (input("Guess a number between 1 and 100: "))

            if guess.isdigit() and guess > num:
                print("Too high!")
                i += 1
            elif guess.isdigit() and guess < num:
                print("Too low!")
                i += 1
            elif guess.isstring :
            else:
                print("Correct!")
                break
        except ValueError:
            print("That's not a number...")

main()
